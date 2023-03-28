import serial
import csv
import time

# Initialize serial communication with the Arduino Uno
ser = serial.Serial('/dev/ttyACM0', 9600) # replace with your serial port and baud rate

# Create a CSV file and write the header row
with open('accelerometer.csv', 'w', newline='') as csvfile: # replace with your desired filename
    writer = csv.writer(csvfile)
    writer.writerow(['x', 'y', 'z'])

    # Collect data for 10 seconds
    start_time = time.time()
    while time.time() - start_time < 10:
        # Read data from the serial port
        line = ser.readline().strip().decode()
        # Parse the data
        x, y, z = [float(v) for v in line.split(',')]
        # Write the data to the CSV file
        writer.writerow([x, y, z])
        # Wait for a short time to avoid overloading the serial port
        time.sleep(0.1)
