import json

with open("phone.json", "r") as fayl:
    telefon = json.load(fayl)

print("Model:", telefon["model"])

narx = int(input("Yangi narxni kiriting: "))

telefon["narx"] = narx

with open("phone.json", "w") as fayl:
    json.dump(telefon, fayl, indent=4)

print("Narx yangilandi!")