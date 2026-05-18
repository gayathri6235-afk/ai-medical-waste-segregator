#include <Servo.h>

Servo servoA;   // Servo for waste type A
Servo servoB;   // Servo for waste type B

char data;

void setup() {
  Serial.begin(9600);

  servoA.attach(9);
  servoB.attach(10);

  // Initial position
  servoA.write(90);
  servoB.write(90);

  Serial.println("Send 'a' or 'b' to control servos");
}

void loop() {
  if (Serial.available()) {
    data = Serial.read();

    if (data == 'a') {
      servoA.write(0);     // Rotate Servo A
      servoB.write(90);    // Keep Servo B idle
      Serial.println("Servo A ON");
      delay(1000);
      servoA.write(90);    // Back to center
    }

    else if (data == 'b') {
      servoB.write(180);   // Rotate Servo B
      servoA.write(90);    // Keep Servo A idle
      Serial.println("Servo B ON");
      delay(1000);
      servoB.write(90);    // Back to center
    }
  }
}
