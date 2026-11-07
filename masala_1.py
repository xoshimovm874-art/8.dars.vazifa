import json

with open("user.json", "r") as fayl:
    malumot = json.load(fayl)

print("Ism:", malumot["ism"])
print("Yosh:", malumot["yosh"])
print("Shahar:", malumot["shahar"])