# include <Servo.h>

// Servo.h 라이브러리에 내장된 Servo 클래스로 실제 서보 모터 제어를 위한 myServo 객체 생성
Servo myServo;

void setup() {
  Serial.begin(9600);
  myServo.attach(10);
}

void loop() {
  for (int angle = 0; angle<=180; angle++) {
    myServo.write(angle);
    Serial.print('angle: ');
    Serial.println(angle);
    delay(100);
  }
}
