void setup() {
  pinMode(3, OUTPUT);
}

void loop() {
  analogWrite(3, 0);
  delay(1000);

  analogWrite(3, 64);
  delay(1000);

  analogWrite(3, 128);
  delay(1000);

  analogWrite(3, 192);
  delay(1000);

  analogWrite(3, 255);
  delay(1000);
}