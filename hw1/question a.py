import csv
count = 0

with open('College.csv', newline='') as csvfile:
    college = csv.reader(csvfile, quotechar='|')
    print("**start read college.csv**")
    for row in college:
        if count > 0:
            print(', '. join(row))
        count += 1
