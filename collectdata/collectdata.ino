#include <Nano33BLE_System.h>

#define CS 9

#include <SPI.h>
#include <ADXL362.h>

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

  Serial.println(z);

  delay(1);
}
