#include <Nano33BLE_System.h>

#define CS 10

#include <SPI.h>
#include <ADXL362.h>

ADXL362 accelerometer;
float a = 0.00;
float b = 1.67423172e-02;
float c = 1.67423172e-02;
float d = 0.00;
float e = 9.66522217e-01;
int16_t unfilteredZ = {0,0,0};
int16_t filteredZ = {0,0,0};

void setup(void)
{
    Serial.begin(9600); 
    accelerometer.begin(CS); 
    accelerometer.beginMeasure(); 
}

void loop()
{
  int16_t x, y, z, t;
  unfilteredZ[2] = unfilteredZ [1];
  unfilteredZ [1] = unfilteredZ [0];
  zFiltered[2] = zFiltered[1];
  zFiltered[1] = zFiltered[0];
  accelerometer.readXYZTData(x, y, unfilteredZ, t);

  filteredZ[0] = a * unfilteredZ[2] + b * unfilteredZ[1] + c * unfilteredZ[0] + d * unfilteredZ[2] + e * unfilteredZ[1];  

  Serial.println(filteredZ);

  delay(1);
}    
