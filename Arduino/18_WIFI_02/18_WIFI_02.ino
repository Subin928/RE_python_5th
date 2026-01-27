#include <SoftwareSerial.h>

SoftwareSerial myESP(2, 3); // D2=RX(ESP TX), D3=TX(ESP RX)

// ESP 모듈 속도가 9600으로 바뀌었는지 확인

void setup() {
  Serial.begin(9600);
  myESP.begin(9600);
  Serial.println("=== TEST 9600 ===");
}

void loop() {
  if (myESP.available()) {
    Serial.write(myESP.read());
  }
  if (Serial.available()) {
    myESP.write(Serial.read());
  }
}

/*
=== TEST 9600 ===
AT

OK
AT+CWLAP
+CWLAP:(3,"U+Net651C",-88,"80:ca:4b:88:65:1e",6,-22,0,4,4,7,0)
+CWLAP:(3,"SK_WiFiGIGA82C2_2.4G",-92,"50:46:ae:53:82:c5",7,-16,0,4,4,7,1)
+CWLAP:(4,"LGWiFi_4C4E",-79,"28:4e:e9:55:4c:51",1,-7,0,4,4,7,0)
+CWLAP:(2,"",-78,"2e:4e:e9:55:4c:51",1,-7,0,3,3,3,0)
+CWLAP:(3,"[LG_Wall-Mount A/C]a7cf",-90,"da:e3:5e:33:a7:cf",11,-9,0,4,4,7,1)
+CWLAP:(3,"U+Net6E6C",-94,"54:7e:1a:a4:4f:f0",11,-4,0,4,4,7,0)
+CWLAP:(3,"DLive_4EED",-85,"bc:62:ce:1e:4e:f2",11,-9,0,4,4,7,0)

OK
AT+CWJAP="spreatics_gusan_cctv","spreatics*"
WIFI CONNECTED
WIFI GOT IP

OK
*/