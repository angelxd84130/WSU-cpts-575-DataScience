import csv
import matplotlib.pyplot as plt

Top = []
Untop = []
count = 0

with open('College.csv', newline='') as csvfile:
    college = csv.reader(csvfile, quotechar='|')
    print("**start read college.csv**")
    for row in college:
        if count > 0:
            if int(row[6]) <= 50:
                Untop.append(int(row[3]) / int(row[2]))
            elif int(row[6]) > 50:
                Top.append(int(row[3]) / int(row[2]))
        count += 1

Top.sort()
Untop.sort()

plt.title("Top School v.s. Untop School")
plt.boxplot([Top, Untop])
plt.xticks((1, 2), ('Top', 'Untop'))
plt.xlabel("School")
plt.ylabel("Acceptance rate")
plt.show()
print("There are", len(Top), "top universities")
