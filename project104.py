import csv
import numpy as np

with open("hwkraggle.csv") as csv_file:
    csv_reader = csv.reader(csv_file)
    list_of_data = list(csv_reader)

print(list_of_data)

total_marks = 0
total_entries = len(list_of_data)

for data in list_of_data:
    total_marks += float(data[1])

mean1 = total_marks / total_entries
print("Mean (Average) is -> " + str(mean1))
