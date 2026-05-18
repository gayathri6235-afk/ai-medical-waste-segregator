https://github.com/gayathri6235-afk/ai-medical-waste-segregator/new/main# 🤖 AI-Based Medical Waste Segregator

> A Final Year B.Tech Project — Department of Electronics and Communication Engineering  
> Government Engineering College, Wayanad | APJ Abdul Kalam Technological University | March 2026

---

## 👥 Team Members

| Name | Roll Number |
|---|---|
| Dhrisyendhu Mukilraj P.G. | WYD22EC044 |
| Gayathri S. | WYD22EC050 |
| Hamna N.V. | WYD22EC054 |
| Nandakumar U. | WYD22EC082 |

**Project Guide:** Dr. Sindhu P., Assistant Professor, ECE Department, GEC Wayanad

---

## 📌 Overview

Improper segregation of biomedical waste poses serious health and environmental risks in healthcare facilities. This project presents an AI-based smart medical waste segregator that automates the classification and disposal of hazardous materials using image processing and embedded control.

A camera module integrated with a Raspberry Pi captures real-time images of waste items such as gloves, masks, and syringes. These images are analyzed using a pre-trained **YOLOv8 (You Only Look Once)** model to classify waste into predefined biomedical categories. Based on the classification, servo motors are triggered to direct the waste into the appropriate bins — ensuring safe, accurate, and contactless disposal.

---

## ✨ Features

- Real-time waste detection using **YOLOv8** deep learning model
- Classifies 13 categories of biomedical waste automatically
- Servo motor controlled bin rotation for contactless segregation
- Real-time web-based monitoring interface (Flask Server)
- Wi-Fi based communication for data logging and remote monitoring
- UV Sterilization Unit integrated into the system
- Manual and Auto mode switching via monitoring interface
- Extendable to cloud platforms for centralized hospital waste tracking
- Low-cost solution (Total cost: ₹10,200/-)

---

## 🗂️ Waste Categories Classified

The system classifies the following 13 types of biomedical waste:

| Category | Type |
|---|---|
| Syringe | Sharps |
| Needle | Sharps |
| Scalpel | Sharps |
| Scissors | Sharps |
| Ampule | Glass |
| Broken Ampule | Glass |
| Gloves | Plastic |
| Mask | Infectious |
| Bandage | Infectious |
| Cotton | Infectious |
| IV Tube | Plastic |
| Expired Medicines | Infectious |

---

## 🏗️ System Architecture / Block Diagram

```
Waste Input
     ↓
Camera Module (RPi Camera Module 3)
     ↓
AI Model (YOLOv8) ←── Power Supply Unit
     ↓
Microcontroller (Raspberry Pi 4)
     ↓                    ↓
Microcontroller       Flask Server
  (Arduino)          (Web Interface)
     ↓
Actuator (Servo Motor)
     ↓
Waste Bins: Sharps | Infectious | Plastics | Pharmaceutical
     ↓
UV Sterilization Unit
```

---

## 🛠️ Hardware Components & Cost

| Component | Quantity | Approx. Cost (₹) |
|---|---|---|
| Raspberry Pi 4 (8 GB) | 1 | 8,200 |
| Raspberry Pi Camera Module 3 | 1 | 241 |
| Arduino UNO Nano | 1 | 330 |
| Servo Motor | 2 | 150 |
| Resin Sheet (Chassis / Frame) | 1 | 500 |
| Power Supply (12V, 2A Adapter) | 1 | 400 |
| Misc. Electronic Components | — | 1,000 |
| **Total Estimated Cost** | | **₹10,200/-** |

---

## 🔧 Component Details

### Raspberry Pi 4 (8GB)
Acts as the central processing unit — handles image acquisition, runs the YOLOv8 model, and controls the entire classification system for real-time detection and segregation.

### Raspberry Pi Camera Module 3
Provides high-quality image capture with improved low-light performance and autofocus. Connects via the CSI interface and captures real-time images of waste items for AI-based analysis.

### YOLOv8 (You Only Look Once – Version 8)
State-of-the-art deep learning model for real-time object detection and classification. Provides high accuracy and fast processing speed for identifying different categories of biomedical waste.

### Arduino UNO Nano
Acts as the interface between Raspberry Pi and servo motors — receives classification signals from the Pi and translates them into precise motor control commands for proper waste bin rotation.

### Servo Motors
Precise actuators that rotate to specific angular positions based on control signals, used to operate mechanical flaps/bin lids to direct waste into the correct bins.

---

## 🧠 AI Model & Dataset

### Dataset
- **Total Images:** 360 labelled images of biomedical waste items
- **Classes:** Syringe, Gloves, Cotton, Scalpel, Scissors, Expired Medicines, Needles, Ampules, Masks, Bandage, IV Tube, Broken Ampule

| Split | Percentage | Images |
|---|---|---|
| Training | 70% | 252 |
| Validation | 20% | 72 |
| Testing | 10% | 36 |

### Model Performance

| Metric | Value |
|---|---|
| Overall Precision | **99.6%** |
| Overall Recall | **99.6%** |
| mAP@50 | **99.5%** |
| mAP@50–95 | **83.0%** |

**Class-wise accuracy:**
- High accuracy (87–90%): Masks, IV Tubes, Scissors
- Moderate accuracy (73–75%): Needles, Scalpels (scope for further augmentation)

---

## ⚙️ How It Works

1. **Waste Placement** — Waste item is placed at the input point
2. **Image Capture** — Raspberry Pi Camera Module 3 captures a real-time image
3. **AI Classification** — YOLOv8 model running on Raspberry Pi 4 classifies the waste type
4. **Signal Transmission** — Raspberry Pi sends classification result to Arduino UNO Nano
5. **Bin Rotation** — Arduino triggers the servo motor to rotate the correct bin into position
6. **Waste Disposal** — Waste falls into the appropriate bin (Sharps / Infectious / Pharmaceutical)
7. **UV Sterilization** — UV unit sterilizes the disposal area
8. **Remote Monitoring** — Flask-based web interface enables real-time monitoring and manual override

---

## 💻 Tech Stack

| Layer | Technology |
|---|---|
| AI Model | YOLOv8 (Ultralytics) |
| Image Processing | Python, OpenCV |
| Backend / Web Interface | Python Flask |
| Microcontroller (Main) | Raspberry Pi 4 (Python) |
| Microcontroller (Motor) | Arduino UNO Nano (C++) |
| Communication | Wi-Fi (HTTP) |
| Hardware Interface | GPIO, Serial (UART) |

---

## 📷 Project Photos

> *(Add actual photos from your project here)*

![AI Medical Waste Segregator](docs/hardware_setup.jpg)
*Figure: AI Based Medical Waste Segregator — Physical Prototype*


---

## 🚀 How to Run

### Prerequisites
```bash
pip install ultralytics opencv-python flask pyserial
```

### Steps
1. Connect Raspberry Pi Camera Module 3 via CSI interface
2. Connect Arduino UNO Nano to Raspberry Pi via USB
3. Upload servo control code to Arduino using Arduino IDE
4. Run the main detection script on Raspberry Pi:
   ```bash
   python main.py
   ```
5. Open the Flask web interface in browser:
   ```
   http://<raspberry-pi-ip>:5000
   ```
6. Select **Auto** mode for AI-based detection or **Manual** mode for manual bin control

---

## 📊 Results

The developed system successfully identifies and classifies different types of medical waste using real-time image capture. Based on the detected object, the system automatically rotates the appropriate bin to ensure correct waste disposal. The real-time monitoring interface enables continuous tracking and improves operational efficiency.

The system demonstrates reliable performance with **99.6% precision and recall**, making it effective for automated medical waste management in healthcare facilities.

---

## 🔭 Future Scope

- Enhanced dataset augmentation for improved needle and scalpel detection
- Multiple camera integration for better angle coverage
- Solar power utilization for sustainability
- Cloud platform integration for centralized hospital waste analytics
- GSM-based alert system for bin-full notifications

---

## 📚 References

1. Moktar et al., "Medical Waste Sorting Machine Development with IoT and YOLO Model Utilization," *J. Eng. Appl. Sci.* 72, 86 (2025). https://doi.org/10.1186/s44147-025-00661-5
2. H. Zhou et al., "A Deep Learning Approach for Medical Waste Classification," *Scientific Reports*, vol. 12, 2022. https://doi.org/10.1038/s41598-022-06146-2
3. K. Gayathri Devi et al., "Automatic Health Care Waste Segregation and Disposal System," *Journal of Xidian University*, vol. 14, no. 5, 2020. https://doi.org/10.37896/jxu14.5/573

---

## 🏫 Institution

**Department of Electronics and Communication Engineering**  
Government Engineering College, Wayanad  
APJ Abdul Kalam Technological University, Kerala  
March 2026
