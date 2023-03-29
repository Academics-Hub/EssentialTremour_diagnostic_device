#include <Wire.h>
#include </home/jono/EssentialTremour_diagnostic_device/collectdata/ACL2.h>

ACL2 accel;

unsigned long startTime; // variable to store the start time

void setup() {
  Serial.begin(9600);
  Wire.begin();
  accel.begin();
  startTime = millis(); // store the current time as the start time
}

void loop() {
  unsigned long elapsedTime = millis() - startTime; // calculate the elapsed time
  if (elapsedTime >= 10000) { // check if elapsed time has exceeded 10 seconds
    return; // exit the loop
  }
  sensors_event_t event;
  accel.getEvent(&event);
  Serial.print(elapsedTime/1000.0); // print elapsed time in seconds
  Serial.print(",");
  Serial.println(event.acceleration.x);
  delay(10);
}



