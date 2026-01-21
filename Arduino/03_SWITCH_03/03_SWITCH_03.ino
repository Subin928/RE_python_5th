int switch1 = 12;
int ledRed = 4;

void setup() {
  Serial.begin(9600);
  pinMode(switch1, INPUT_PULLUP);
  pinMode(ledRed, OUTPUT);
}

void loop() {
  int SW1 = digitalRead(switch1);
  digitalWrite(ledRed, LOW);

  if(SW1 == LOW) {
    Serial.println("Switch : RED");
    digitalWrite(ledRed, HIGH);
  }
  delay(100);
}
  