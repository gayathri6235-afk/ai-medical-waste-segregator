from flask import Flask, render_template_string, Response, request
import cv2
import threading
import time
import numpy as np
import os
from picamera2 import Picamera2
from robo import Control

# ---- prevent numpy crash on Pi ----
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"

app = Flask(__name__)
control = Control()

frame_lock = threading.Lock()
shared_frame = None
detect_box = None
detect_label = None

# ==============================
# LOAD ONNX MODEL
# ==============================
net = cv2.dnn.readNet("model.onnx")
INPUT_SIZE = 640

# ==============================
# CAMERA
# ==============================
picam2 = Picamera2()
config = picam2.create_video_configuration(
    main={"size": (640, 480), "format": "RGB888"}
)
picam2.configure(config)
picam2.start()
time.sleep(2)

# ==============================
# DETECTION
# ==============================
def detect(frame):
    h, w = frame.shape[:2]

    blob = cv2.dnn.blobFromImage(
        frame, 1/255.0,
        (INPUT_SIZE, INPUT_SIZE),
        swapRB=True, crop=False
    )

    net.setInput(blob)
    preds = net.forward()

    detections = []

    for det in preds[0]:
        score = float(det[4])
        if score < 0.4:
            continue

        cls_id = int(det[5])
        x, y, bw, bh = det[0:4]

        x1 = int((x - bw/2) * w)
        y1 = int((y - bh/2) * h)
        x2 = int((x + bw/2) * w)
        y2 = int((y + bh/2) * h)

        detections.append({
            "label": str(cls_id),
            "conf": score,
            "box": (x1, y1, x2-x1, y2-y1)
        })

    return detections

# ==============================
# AI THREAD (optional auto logic)
# ==============================
def detect_thread():
    global shared_frame, detect_box, detect_label

    while True:
        with frame_lock:
            if shared_frame is None:
                time.sleep(0.05)
                continue
            frame = shared_frame.copy()

        detections = detect(frame)

        detect_box = None
        detect_label = None

        for d in detections:
            detect_label = d["label"]
            detect_box = d["box"]
            break

        time.sleep(0.1)

# ==============================
# STREAM
# ==============================
def gen_frames():
    global shared_frame

    while True:
        frame = picam2.capture_array()

        with frame_lock:
            shared_frame = frame.copy()

        if detect_box:
            x,y,w,h = detect_box
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

        if detect_label:
            cv2.putText(frame, detect_label,(20,40),
                        cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# ==============================
# WEB ROUTES
# ==============================
@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(),
        mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
    return render_template_string("""
<!DOCTYPE html>
<html>
<head>
<title>Medical Waste</title>

<style>
body{
    margin:0;
    background:linear-gradient(135deg,#0f2027,#203a43,#2c5364);
    font-family:Arial,Helvetica,sans-serif;
    color:white;
    text-align:center;
}

.header{
    font-size:36px;
    padding:20px;
    font-weight:bold;
    letter-spacing:2px;
}

.container{
    display:flex;
    flex-direction:column;
    align-items:center;
}

.video-box{
    border-radius:20px;
    overflow:hidden;
    box-shadow:0 0 25px rgba(0,255,200,0.4);
    margin-top:10px;
}

.controls{
    margin-top:25px;
}

button{
    width:150px;
    height:65px;
    margin:12px;
    border:none;
    border-radius:14px;
    font-size:20px;
    font-weight:bold;
    cursor:pointer;
    transition:0.2s;
}

button:hover{
    transform:scale(1.05);
}

.bin1{background:#e53935;}
.bin2{background:#1e88e5;}
.bin3{background:#43a047;}
.bin4{background:#fb8c00;}

.footer{
    margin-top:25px;
    font-size:14px;
    opacity:0.6;
}
</style>
</head>

<body>

<div class="header">
MEDICAL WASTE SEGREGATOR
</div>

<div class="container">

<div class="video-box">
<img src="/video_feed" width="640">
</div>

<div class="controls">
<form action="/bin" method="post">
    <button class="bin1" name="b" value="1">BIN 1</button>
    <button class="bin2" name="b" value="2">BIN 2</button><br>
    <button class="bin3" name="b" value="3">BIN 3</button>
    <button class="bin4" name="b" value="4">BIN 4</button>
</form>
</div>

<div class="footer">
AI SYSTEM GECW
</div>

</div>

</body>
</html>
""")


@app.route('/bin', methods=['POST'])
def bin_control():
    b = request.form['b']

    if b == "1":
        print("BIN 1")
        control.left()

    elif b == "2":
        print("BIN 2")
        control.right()

    elif b == "3":
        print("BIN 3")
        control.forward()

    elif b == "4":
        print("BIN 4")
        control.stop()

    return ('',204)

# ==============================
# MAIN
# ==============================
if __name__ == '__main__':
    threading.Thread(target=detect_thread, daemon=True).start()
    app.run(host='0.0.0.0', port=5000, debug=False)
