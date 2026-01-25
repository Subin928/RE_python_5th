#include <Servo.h>
#include <LiquidCrystal_I2C.h>

Servo myServo;
LiquidCrystal_I2C myLcd(0x27, 16, 2);

int angle = 0;

void setup() {
  myServo.attach(8);
  myLcd.init();
  myLcd.backlight();
}

void loop() {
  int angleVal = analogRead(A0);
  angle = map(angleVal, 0, 1023, 0, 180);

  myServo.write(angle);

  myLcd.setCursor(0, 0);
  myLcd.print("Servo Angle");
  myLcd.setCursor(0, 1);
  myLcd.print(angle);
  delay(500);

  myLcd.clear();
}
