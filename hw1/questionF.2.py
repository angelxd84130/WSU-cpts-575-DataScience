import csv
import matplotlib.pyplot as plt
import seaborn as sns


PublicSchoolF = []
PublicSchoolP = []
PrivateSchoolF = []
PrivateSchoolP = []


with open('College.csv', newline='') as csvfile:
    college = csv.reader(csvfile, quotechar='|')
    for row in college:
        if row[1] == "Yes":
            PrivateSchoolF.append(int(row[7]))
            PrivateSchoolP.append(int(row[8]))
        elif row[1] == "No":
            PublicSchoolF.append(int(row[7]))
            PublicSchoolP.append(int(row[8]))

plt.title("college")
#plt.hist(PrivateSchool, density=1, bins=60, label='PrivateSchool', color='red', stacked=True, alpha = 0.5)
#plt.hist(PublicSchool, density=1, bins=60, label='PublicSchool', color='blue', stacked=True, alpha = 0.5)
#sns.distplot(PrivateSchool, rug=True, hist=False)
#sns.distplot(PublicSchool, rug=True, hist=False)

#plt.xlabel("The number os students")
#plt.ylabel("Probability")
labels = "Private Full Time", "Private Part Time", "Public Full Time", "Public Part Time"
FullStudents = sum(PrivateSchoolP)+sum(PrivateSchoolF)+sum(PublicSchoolP)+sum(PublicSchoolF)
sizes = [sum(PrivateSchoolF)/FullStudents, sum(PrivateSchoolP)/FullStudents, sum(PublicSchoolF)/FullStudents, sum(PublicSchoolP)/FullStudents]
#sizes = [215, 130, 245, 210]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
#explode = (0.1, 0, 0, 0)
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.legend()
plt.show()