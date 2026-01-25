#include <SPI.h>
#include <MFRC522.h>

#define SS_PIN 10
#define RST_PIN 9

MFRC522 myMFRC(SS_PIN, RST_PIN);

int LED_B = 3;
int LED_R = 4;
int PIEZO = 6;

void setup() {
  Serial.begin(9600);
  SPI.begin();
  pinMode(SS_PIN, OUTPUT);
  myMFRC.PCD_Init();

  pinMode(LED_B, OUTPUT);
  pinMode(LED_R, OUTPUT);
  pinMode(PIEZO, OUTPUT);

  Serial.println("RFID 준비 완료");

  myMFRC.PICC_HaltA();
  myMFRC.PCD_StopCrypto1();
  delay(1000);
}

void loop() {
  if (!myMFRC.PICC_IsNewCardPresent()) 
    return;
  if (!myMFRC.PICC_ReadCardSerial())
    return;

  Serial.print("UID: ");
  for (byte i = 0; i < myMFRC.uid.size; i++) {
    Serial.print(myMFRC.uid.uidByte[i]);
    Serial.print(" ");
  }
  Serial.println("");

  if(myMFRC.uid.uidByte[0] == 53 && myMFRC.uid.uidByte[1] == 38
      && myMFRC.uid.uidByte[2] == 198 && myMFRC.uid.uidByte[3] == 1) {
    digitalWrite(LED_B, HIGH);
    digitalWrite(LED_R, LOW);
    Serial.println("Hello, Blue LED Pin!");
    digitalWrite(PIEZO, HIGH);
    delay(300);
    digitalWrite(PIEZO, LOW);
    digitalWrite(LED_B, LOW);
    } else {
      digitalWrite(LED_R, HIGH);
      digitalWrite(LED_B, LOW);
      Serial.println("Error!");
     
      digitalWrite(PIEZO, HIGH);
      delay(300);
    
      digitalWrite(PIEZO, LOW);
      delay(200);
     
      digitalWrite(PIEZO, HIGH);
      delay(500);
      digitalWrite(PIEZO, LOW);
      digitalWrite(LED_R, LOW);
    }
}
/*
UID: 53 38 198 1 
Hello, Blue LED Pin!
UID: 113 98 91 93 
Error!
*/
