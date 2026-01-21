int BTN = 12;

void setup() {
  Serial.begin(9600);
  pinMode(BTN, INPUT_PULLUP); // 기본 상태가 1(HIGH, 5V), 스위치가 눌렸을 때 0(LOW, 0V)
}

void loop() {
  int BTNState = digitalRead(BTN);
  Serial.println(BTNState);
  delay(500);
}
