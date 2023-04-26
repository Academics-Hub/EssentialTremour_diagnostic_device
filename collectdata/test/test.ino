#include <Nano33BLE_System.h>

#include <SPI.h>

/************************************************************************

  Test of Pmod ACL2

*************************************************************************

  Description: Pmod_ACL2
  The 3 components X, Y, and Z of the acceleration, and the temperature
  are displayed in the serial monitor.

  Material
  1. Arduino Uno
  2. Pmod ACL2 (dowload library https://github.com/annem/ADXL362 )
  3. Adafruit TXB0108

  Wiring
  Module<----------> Arduino
  VCC     to        3V3
  GND     to        GND
  SCK     to        13 (SCK)
  MOSI    to        12 (MOSI)
  MISO    to        11 (MIS0)
  CS      to        10

  a logic level converter must be used!!!

************************************************************************/

#define CS 9 //chip select pin

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
  Serial.print("x = ");
  Serial.print(x);
  Serial.print("\t y = ");
  Serial.print(y);
  Serial.print("\t z = ");
  Serial.print(z);
  Serial.print("\t t = ");
  Serial.println(t);

  //wait 0.5s before next aquisition
  delay(1);
}
