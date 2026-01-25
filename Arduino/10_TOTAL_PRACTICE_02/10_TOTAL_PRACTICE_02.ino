#define RED 4
#define GREEN 5
#define BLUE 6

void setup() {
  pinMode(RED, OUTPUT);
  pinMode(GREEN, OUTPUT);
  pinMode(BLUE, OUTPUT);
}

void loop() {
  int gasValue = analogRead(GAS_AO);

  digitalWrite(RED, LOW);
  digitalWrite(GREEN, LOW);
  digitalWrite(BLUE, LOW);

  if (gasValue < 300) {
    digitalWrite(BLUE, HIGH);
  }
  else if (gasValue < 500) {
    digitalWrite(GREEN, HIGH);
  }
  else {
    digitalWrite(RED< HIGH);
  }
  delay(500);
}