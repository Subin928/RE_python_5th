int LED_BLUE = 10;
int LED_GREEN = 11;
int LED_RED = 12;

void setup() {
  pinMode(LED_BLUE, OUTPUT);
  pinMode(LED_GREEN, OUTPUT);
  pinMode(LED_RED, OUTPUT);
}

// 버전 2: 모든 LED가 켜진 뒤 0.5초 동안 유지하고, 모든 LED를 끈 뒤 0.5초 유지
void loop() {
  digitalWrite(LED_RED, HIGH);                           
  digitalWrite(LED_GREEN, HIGH);
  digitalWrite(LED_BLUE, HIGH);
  delay(500);

  digitalWrite(LED_RED, LOW);                      
  digitalWrite(LED_GREEN, LOW);
  digitalWrite(LED_BLUE, LOW);
  delay(500);                 
}