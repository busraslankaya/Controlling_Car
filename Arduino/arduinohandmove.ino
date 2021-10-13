#include <SoftwareSerial.h>
SoftwareSerial Bluetooth(3, 2); // RX TX BLUETOOTH

#define in1 11
#define in2 10
#define in3 9
#define in4 8

char state;
void setup() {
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);
  Bluetooth.begin(9600);
  Serial.begin(9600);

  //forward();
}
void loop() {
  if (Bluetooth.available()) {
    state = Bluetooth.read();


    if (state == '1') {
      forward();
      
      // Bluetooth.println("forward");

    }
    if (state == '2') {
      back();
      //Bluetooth.println("backward");

    }
    if (state == '3') {
      left();
      // Bluetooth.println("left");

    }
    if (state == '4') {
      right();
      // Bluetooth.println("right");

    }
    if (state == '5') {
      //Bluetooth.println("stop");
      Stop();
    }

  }
}
void forward() {
  analogWrite(in1, 250);
  analogWrite(in3, 250);
}
void back() {
  analogWrite(in2, 255);
  analogWrite(in4, 255);
}
void left() {
  analogWrite(in4, 255);
  analogWrite(in1, 255);
}
void right() {
  analogWrite(in3, 255);
  analogWrite(in2, 255);
}
void Stop() {
  analogWrite(in1, 0);
  analogWrite(in2, 0);
  analogWrite(in3, 0);
  analogWrite(in4, 0);
}
