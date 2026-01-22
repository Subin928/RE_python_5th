void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT); // LED
}

void loop() {
  int light = analogRead(A0);
  Serial.println(light);

  if (light > 500)
    digitalWrite(13, HIGH);
  else
    digitalWrite(13, LOW);
}
// 값이 클수록 어두움