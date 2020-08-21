import csv
import matplotlib.pyplot as plt

listMedian = []
count = 0

with open('College.csv', newline='') as csvfile:
    college = csv.reader(csvfile, quotechar='|')
    for row in college:
        if count > 0:
            listMedian.append(int(row[11]))
        count += 1

listMedian.sort()
print("The median cost of books for all schools in "
      "this dataset is: ", listMedian[int(count/2)])
