int brightness = 0;

void setup() {
  Serial.begin(9600);
  pinMode(3, OUTPUT);
}

void loop() {
  for (brightness = 0; brightness < 256; brightness++) {
    analogWrite(3, brightness);
    delay(10); // 0.01초마다 밝아짐
    Serial.println(brightness); // println: 출력 + 줄바꿈
  }
}

/*
Serial: 시리얼통신을 담당하는 객체
  시리얼 통신: 글자, 숫자, 데이터를 주고받는 통신

Serial.begin(9600);
- 아두이노가 PC와 통신하기 위해 시리얼 통신을 시작하겠다 명시하는 코드
- 매개변수로 넣은 값 속도로 시리얼 통신을 시작함
- 통신 속도는 대체로 9600을 사용
  - 오래전부터 사용해온 안정적이고 에러 없는 표준 속도
    - 통신 속도가 너무 빠르면 데이터 손실이 생기고, 느리면 데이터 전송이 불편
  - 거의 모든 장치가 지원하는 속도
- setup() 함수 내에 한 번만 작성하면 됨

Serial.print()
- 아두이노에서 PC(시리얼 모니터)로 문자나 숫자, 변수값을 보내주는 함수
- 통신 상태 확인 or 디버깅용으로 사용
*/