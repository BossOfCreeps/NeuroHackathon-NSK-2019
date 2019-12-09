#include <Servo.h>

Servo myservo;

void setup() {
  Serial.begin(9600);
  myservo.attach(9);
       myservo.write(90); 
}

void loop() {
  if(Serial.available() > 0) {
    char data = Serial.read();
    char str[2];
    str[0] = data;
    if (data=='0')
       myservo.write(100);
    if (data=='1')
       myservo.write(120); 
    str[1] = '\0';
    Serial.print(str);
  }
}
