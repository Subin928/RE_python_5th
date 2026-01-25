#include <DHT.h>

#define DHTPIN 2
#define DHTTYPE DHT22
#define GAS_A A0

#define LED_R 3
#define LED_G 4
#define LED_B 5

#define ECHO_PIN 6
#define TRIG_PIN 7

#define SWITCH_PIN 8
#define FIEZO_PIN 9

DHT mydht(DHTPIN, DHTTYPE);

bool isDanger = false; // 가스 농도가 600 이상인 경우 true로 전환

float getDistance() { // 실수 값을 반환하는 함수를 만들 때
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);
  
  float duration = pulseIn(ECHO_PIN, HIGH);
  float distance = ((34000*duration)/1000000)/2;

  return distance; // 초음파센서가 측정한 거리 값을 받음
}

void setup() {
  Serial.begin(9600);
  mydht.begin();

  pinMode(GAS_A, INPUT);

  pinMode(LED_R, OUTPUT);
  pinMode(LED_G, OUTPUT);
  pinMode(LED_B, OUTPUT);

  pinMode(ECHO_PIN, INPUT);
  pinMode(TRIG_PIN, OUTPUT);

  pinMode(SWITCH_PIN, INPUT_PULLUP); // 기본적으로 HIGH
  pinMode(FIEZO_PIN, OUTPUT);
}

void loop() {
  // 온습도 시리얼 모니터에 출력
  float h = mydht.readHumidity(); // 습도
  float c = mydht.readTemperature(); // 온도

  // 가스 센서 AO값 출력
  int gasVal = analogRead(GAS_A);

  // 초음파센서 거리
  float distance = getDistance();

  // 스위치 상태 (눌렸을 때 LOW)
  int switchState = digitalRead(SWITCH_PIN);

  // 초음파센서로 5cm 거리에 물체 존재 여부 확인
  isDanger = false;

  Serial.print("습도: "+ String(h) + "% 온도: " + String(c) + "°C ");
  Serial.println("가스 농도(AO): " + String(gasVal));
  Serial.println("거리: " + String(distance) + "cm");

  if(gasVal >= 600) {
    isDanger = true;
    // 빨간색 LED ON
    digitalWrite(LED_R, HIGH);
    digitalWrite(LED_G, LOW);
    digitalWrite(LED_B, LOW);
  } else if (gasVal >= 300) {
    // 초록색 LED ON
    digitalWrite(LED_R, LOW);
    digitalWrite(LED_G, HIGH);
    digitalWrite(LED_B, LOW);
  } else {
    // 파란색 LED ON
    digitalWrite(LED_R, LOW);
    digitalWrite(LED_G, LOW);
    digitalWrite(LED_B, HIGH);
  }

  while (isDanger && distance <= 5.0) {
    digitalWrite(LED_R, HIGH);
    delay(100);
    digitalWrite(LED_R, LOW);
    delay(100);

    if(switchState == LOW) {
      digitalWrite(FIEZO_PIN, HIGH);
    } else {
      digitalWrite(FIEZO_PIN, LOW);
    }

    distance = getDistance(); // 무한 루프를 빠져나오는 코드
  }

  delay(500);
}