import csv
import random

# Generate random accelerometer data
data = [(random.uniform(-2, 2), random.uniform(-2, 2), random.uniform(-2, 2)) for _ in range(100)]

# Write the data to a CSV file
with open('accelerometer.csv', 'w', newline='') as csvfile: # replace with your desired filename
    writer = csv.writer(csvfile)
    writer.writerow(['x', 'y', 'z'])
    writer.writerows(data)
