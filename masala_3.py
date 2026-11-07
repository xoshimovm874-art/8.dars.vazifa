import json

with open("student.json", "r") as fayl:
    talaba = json.load(fayl)

talaba["ball"] = 95

with open("student.json", "w") as fayl:
    json.dump(talaba, fayl, indent=4)

print(talaba)