import json

with open("product.json", "r") as fayl:
    mahsulot = json.load(fayl)

umumiy = mahsulot["narx"] * mahsulot["miqdor"]

print("Mahsulot:", mahsulot["nom"])
print("Umumiy qiymati:", umumiy)