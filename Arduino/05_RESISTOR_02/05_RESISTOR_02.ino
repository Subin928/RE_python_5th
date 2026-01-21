void setup() {
  Serial.begin(9600);
  pinMode(10, OUTPUT);
}

void loop() {
  int resistor = analogRead(A0);
  Serial.println(resistor);
  resistor = map(resistor, 0, 1023, 0, 255);
  analogWrite(10, resistor);
  delay(100);
}
