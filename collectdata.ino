#include <Wire.h>
#include <Adafruit_ADXL345.h>

Adafruit_ADXL345 accel = Adafruit_ADXL345();

void setup() {
  Serial.begin(9600);
  Wire.begin();
  accel.begin();
}

void loop() {
  sensors_event_t event;
  accel.getEvent(&event);
  Serial.print(event.acceleration.x);
  Serial.print(",");
  Serial.print(event.acceleration.y);
  Serial.print(",");
  Serial.println(event.acceleration.z);
  delay(10);
}
