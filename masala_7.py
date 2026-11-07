import csv

eng_qimmat = 0
nomi = ""

with open("products.csv", "r") as fayl:
    oqish = csv.DictReader(fayl)

    for mahsulot in oqish:
        narx = int(mahsulot["narx"])
        miqdor = int(mahsulot["miqdor"])

        umumiy = narx * miqdor

        print(mahsulot["nom"], umumiy)

        if narx > eng_qimmat:
            eng_qimmat = narx
            nomi = mahsulot["nom"]

print("Eng qimmat mahsulot:", nomi)