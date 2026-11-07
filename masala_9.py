import csv

jami = 0
soni = 0
eng_katta = 0
nomi = ""

with open("expenses.csv", "r") as fayl:
    oqish = csv.DictReader(fayl)

    for xarajat in oqish:
        summa = int(xarajat["summa"])

        jami += summa
        soni += 1

        if summa > eng_katta:
            eng_katta = summa
            nomi = xarajat["nom"]

print("Jami xarajat:", jami)
print("Eng katta xarajat:", nomi, eng_katta)
print("Xarajatlar soni:", soni)