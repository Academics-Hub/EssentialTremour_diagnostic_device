import serial
import time
import csv

def read(filename):
    ser = serial.Serial('/dev/ttyACM0', 9600)
    time.sleep(2)

    with open('data.csv', 'w') as f:
        writer = csv.writer(f)
        timer = 10
        t = 0
        while timer:
            data = ser.readline().decode().strip()
            writer.writerow([t, data])
            timer -= 0.01
            t += 0.01
            time.sleep(0.01)