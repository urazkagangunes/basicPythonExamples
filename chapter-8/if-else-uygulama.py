# soru 1
# gastype = {
#     'benzin': 39.35,
#     'dizel': 41.71,
#     'lpg': 20.28
# }

# inputGasType = input("Yakıt tipini yazınız. ")
# mile = int(input("Gidilen mesafeyi giriniz: "))

# if(inputGasType == 'benzin'):
#     result = gastype['benzin'] * mile
#     print(f"Benzinli araç için bu mesafenin yakacğaı yakıt: {result}")
# elif(inputGasType == 'lpg'):
#     result = gastype['lpg'] * mile
#     print(f"LPG araç için bu mesafenin yakacğaı yakıt: {result}")
# elif(inputGasType == 'dizel'):
#     result = gastype['dizel'] * mile
#     print(f"Dizel araç için bu mesafenin yakacğaı yakıt: {result}")
# else:
#     print("Lütfen gas tipini doru giriniz.")


# soru2
firstExamResult = int(input("İlk sınav sonucunu gir: "))
secondExamResult = int(input("İkinci sınav sonucunu gir: "))
quizResult = int(input("Quiz sonucunuzu giriniz: "))

avg = (firstExamResult + secondExamResult + quizResult) / 3

if((avg >= 0) and (avg <= 24)):
    print(0)
elif((avg >= 25) and (avg <= 44)):
    print(1)
elif((avg >= 45) and (avg <= 54)):
    print(2)
elif((avg >= 55) and (avg <= 69)):
    print(3)
elif((avg >= 70) and (avg <= 84)):
    print(4)
elif((avg >= 85) and (avg <= 100)):
    print(5)
else:
    print("Girilen notları tekrar kontrol ediniz...") 