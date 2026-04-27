#task2 

import csv
marks = {"math": 20, "science":30}
total = sum(marks.values())
avg = total / len(marks)
with open("marks.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Subject", "Marks"])
   
    for subject, mark in marks.items():
        writer.writerow([subject, mark])
    
    #total and average
    writer.writerow(["total", total])
    writer.writerow(["Average", avg])

    # read
    with open("marks.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)