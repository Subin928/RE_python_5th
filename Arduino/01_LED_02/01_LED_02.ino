int LED_PIN = 3; // 사용할 핀 번호를 변수화

void setup() {
  pinMode(LED_PIN, OUTPUT); // 디지털 3번 핀을 출력으로 사용한다 정의
}

void loop() {
  digitalWrite(LED_PIN, HIGH);  // 3번 핀을 hIGH(5v)로 출력 => LED 켜짐
  delay(1000);                      // LED 켜진 상태로 1초 중지
  digitalWrite(LED_PIN, LOW);   // 3번 핀을 LOW(0v)로 출력 => LED 꺼짐
  delay(1000);                      // LED 꺼진 상태로 1초 중지
}
