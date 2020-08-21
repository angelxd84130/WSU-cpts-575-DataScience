import csv
import matplotlib.pyplot as plt
import numpy as nu

listMedian = []
countMedian = 0
scatterX = []
scatterY1 = []
scatterY2 = []
PublicSchool = []
PrivateSchool = []

with open('College.csv', newline='') as csvfile:
    college = csv.reader(csvfile, quotechar='|')
    for row in college:
        if countMedian > 0:
            listMedian.append(int(row[11]))
            scatterX.append(countMedian)
            scatterY1.append(int(row[7]))
            scatterY2.append(int(row[8]))
            if row[1]=="Yes":
                PrivateSchool
            else:
                PublicSchool
        countMedian += 1
        #print(', '. join(row))

#must start from the 2nd row
listMedian.pop(0)
scatterY1.pop(0)
scatterY2.pop(0)
scatterX.pop()


listMedian.sort()
print("The median cost of books for all schools in this dataset is: ", listMedian[int(countMedian/2)])


plt.title("college")


'''question D'''

plt.scatter(scatterY1, scatterY2, label="Group 1", color="orange", marker="o", s=10)
plt.xlabel('Full-time students')
plt.ylabel('Part-time students')
plt.legend()


plt.show()

