import csv
import matplotlib.pyplot as plt
import seaborn as sns


PublicSchool = []
PrivateSchool = []


with open('College.csv', newline='') as csvfile:
    college = csv.reader(csvfile, quotechar='|')
    for row in college:
        if row[1] == "Yes":
            PrivateSchool.append(int(row[7]) + int(row[8]))
        elif row[1] == "No":
            PublicSchool.append(int(row[7]) + int(row[8]))

plt.title("college")
plt.hist(PrivateSchool, density=1, bins=60, label='PrivateSchool', color='red', stacked=True, alpha = 0.5)
plt.hist(PublicSchool, density=1, bins=60, label='PublicSchool', color='blue', stacked=True, alpha = 0.5)
sns.distplot(PrivateSchool, rug=True, hist=False)
sns.distplot(PublicSchool, rug=True, hist=False)

plt.xlabel("The number os students")
plt.ylabel("Probability")
plt.legend()
plt.show()