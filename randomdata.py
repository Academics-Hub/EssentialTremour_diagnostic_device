import csv
import random
import time

# Generate random accelerometer data for 10 seconds
start_time = time.time()
data = []
while time.time() - start_time < 10:
    data.append((random.uniform(-2, 2), 0, 0))

# Write the data to a CSV file
with open('accelerometer.csv', 'w', newline='') as csvfile: # replace with your desired filename
    writer = csv.writer(csvfile)
    writer.writerow(['time', 'x'])
    for i, (x, _, _) in enumerate(data):
        writer.writerow([i/10.0, x])
