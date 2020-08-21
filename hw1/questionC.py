import csv
import matplotlib.pyplot as plt

count = 0
FullTimeStudent = []
PartTimeStudent = []

with open('College.csv', newline='') as csvfile:
    college = csv.reader(csvfile, quotechar='|')
    for row in college:
        if count > 0:
            FullTimeStudent.append(int(row[7]))
            PartTimeStudent.append(int(row[8]))
        count += 1

plt.title("college")
plt.scatter(FullTimeStudent, PartTimeStudent, label="Group 1",
            color="orange", marker="o", s=10)
plt.xlabel('Full-time students')
plt.ylabel('Part-time students')
plt.show()

