#include <Nano33BLE_System.h>
#include <SPI.h>
#include <ADXL362.h>

#define CS 10 
ADXL362 accelerometer;

void setup(void)
{
  Serial.begin(9600);
  accelerometer.begin(CS);
  accelerometer.beginMeasure();
}

void loop()
{
  int16_t x, y, z, t;
  accelerometer.readXYZTData(x, y, z, t);
  Serial.println(y);
  delay(100);
}
