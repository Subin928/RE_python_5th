const int PIEZO_PIN = 8;
const int SWITCH = 2;

void setup() {
  Serial.begin(9600);
  pinMode(PIEZO_PIN, OUTPUT);
  pinMode(SWITCH, INPUT_PULLUP);
}

void loop() {
  int switchState = digitalRead(SWITCH);
  digitalWrite(PIEZO_PIN, LOW);

  if(switchState == LOW) {
    Serial.println("부저 ON");
    digitalWrite(PIEZO_PIN, HIGH);
  } else {
      Serial.println("BUZZER OFF");
  }
  delay(100);
}
