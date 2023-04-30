#include <Nano33BLE_System.h>
#include <SPI.h>
#define CS 10 //chip select pin

// Call of libraries
#include <SPI.h>
#include <ADXL362.h>

ADXL362 accelerometer; // Creation of the object

void setup(void)
{
  Serial.begin(9600); // initialization of serial communication
  accelerometer.begin(CS); // initialization of the accelerometer
  accelerometer.beginMeasure();  //initialization of the measurement
}

void loop()
{
  // Acquisition of accelerometer data
  int16_t x, y, z, t;
  accelerometer.readXYZTData(x, y, z, t);

  //display raw data
  Serial.println(y);

  //wait 0.5s before next aquisition
  delay(50);
}
