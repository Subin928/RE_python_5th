int BTN = 2;

void setup() {
  Serial.begin(9600);
  pinMode(BTN, INPUT);
}

void loop() {
  int BTNState = digitalRead(BTN);
  Serial.println(BTNState);
  delay(500);
}
