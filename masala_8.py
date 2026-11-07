import csv

ism = input("Ism: ")
yosh = input("Yosh: ")
kurs = input("Kurs: ")

with open("students.csv", "a", newline="") as fayl:
    yozish = csv.writer(fayl)
    yozish.writerow([ism, yosh, kurs])

with open("students.csv", "r") as fayl:
    oqish = csv.reader(fayl)

    for qator in oqish:
        print(qator)