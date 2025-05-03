
// Arduino Sketch: gesture_hand.ino

#include <Servo.h>

Servo thumb, index, middle, ring, pinky;

void setup() {
  Serial.begin(9600);
  thumb.attach(3);
  index.attach(5);
  middle.attach(6);
  ring.attach(9);
  pinky.attach(10);
}

void loop() {
  if (Serial.available()) {
    String data = Serial.readStringUntil('\n');
    if (data.length() == 5) {
      thumb.write(data[0] == '1' ? 0 : 90);
      index.write(data[1] == '1' ? 0 : 90);
      middle.write(data[2] == '1' ? 0 : 90);
      ring.write(data[3] == '1' ? 0 : 90);
      pinky.write(data[4] == '1' ? 0 : 90);
    }
  }
}
