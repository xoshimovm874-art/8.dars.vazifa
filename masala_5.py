import json

talaba = {
    "ism": "Sardor",
    "yosh": 20,
    "kurs": 2
}

matn = json.dumps(talaba)

print(matn)

lugat = json.loads(matn)

print("Talaba ismi:", lugat["ism"])