#include <DHT.h>

#define DHTPIN 2
#define DHTTYPE DHT11
#define GAS_AO A0

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();

  Serial.println("가스센서 히터 가열 시작");
  delay(30000);
  Serial.println("측정 시작");
}

void loop() {
  float temp = dht.readTemperature();
  float humi = dht.readHumidity();
  int gasValue = analogRead(GAS_AO);

  Serial.print("온도: ");
  Serial.print(temp);
  Serial.print(" C | 습도: ");
  Serial.print(humi);
  Serial.print(" % | Gas AO: ");
  Serial.println(gasValue);

  delay(1000);
}
