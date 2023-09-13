#include <Arduino.h>
#include <Wire.h>


const int GYRO_ADDR = 8;
const int GRYO_BYTES = 10;



void setup() {
  // put your setup code here, to run once:
  Wire.begin();
  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
  Wire.requestFrom(G
}