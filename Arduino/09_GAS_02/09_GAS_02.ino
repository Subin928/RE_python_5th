#define GAS_AO A0
#define GAS_DO 8
#define PIEZO 12
#define LED 13

void setup() {
  Serial.begin(9600);

  pinMode(GAS_DO, INPUT);
  pinMode(PIEZO, OUTPUT);
  pinMode(LED, OUTPUT);

  Serial.println("히터 가열 시작");
  delay(1000);
  Serial.println("히터 가열 종료 동작 시작");
}

void loop() {
  digitalWrite(PIEZO, LOW);
  digitalWrite(LED, LOW);

  float sensorValue = analogRead(GAS_AO);
  int sensorDValue = digitalRead(GAS_DO);

  Serial.print("아날로그 센서입력: ");
  Serial.print(sensorValue);

  Serial.print(" | ");
  Serial.print("디지털 센서입력: ");
  Serial.println(sensorDValue);

  if (sensorValue > 40) {
    Serial.println("!! 연기 감지 !!");
    digitalWrite(PIEZO, HIGH);
    digitalWrite(LED, HIGH);
  }

  delay(1000);
}