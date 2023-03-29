import serial
import csv
import time

# Initialize serial communication with the Arduino Uno
ser = serial.Serial('COM3', 9600) # replace with your serial port and baud rate

# Create a CSV file and write the header row
with open('accelerometer.csv', 'w', newline='') as csvfile: # replace with your desired filename
    writer = csv.writer(csvfile)
    writer.writerow(['time', 'x'])

    # Collect data for 10 seconds
    start_time = time.time()
    while time.time() - start_time < 10:
        # Read data from the serial port
        line = ser.readline().strip().decode()
        # Parse the data
        time_, x = [float(v) for v in line.split(',')]
        # Write the data to the CSV file
        writer.writerow([time_, x])
        # Wait for a short time to avoid overloading the serial port
        time.sleep(0.1)
