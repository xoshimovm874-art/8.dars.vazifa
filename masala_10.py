import csv

eng_yuqori = 0
eng_yaxshi = ""

with open("sportchilar.csv", "r") as fayl:
    oqish = csv.DictReader(fayl)

    for sportchi in oqish:
        ism = sportchi["ism"]
        sport = sportchi["sport"]
        ball = int(sportchi["ball"])

        print(ism, sport, ball)

        if ball > 80:
            print("80 dan yuqori:", ism)

        if ball > eng_yuqori:
            eng_yuqori = ball
            eng_yaxshi = ism

print("Eng yuqori ball:", eng_yaxshi, eng_yuqori)