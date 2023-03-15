import serial
import time
import csv

ser = serial.Serial('/dev/ttyACM0', 9600)
time.sleep(2)

with open('data.csv', 'w') as f:
    writer = csv.writer(f)
    timer = 0
    while True:
        data = ser.readline().decode().strip()
        writer.writerow([timer, data])
        timer += 0.01
        time.sleep(0.01)