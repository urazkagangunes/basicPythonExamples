Brand = ["Toyota", "BMW", "Renault", "Mercedes"]

result = len(Brand)

result = Brand[0] + Brand[3]

Brand[2] = "TOGG"
# for i in Brand:
    # print(i)

result = "TOGG" in Brand
result = "TOGG" not in Brand

result = Brand[:2]

result = Brand + ["Ford", "Citröen"]
# for i in result:
    # print(i)

del(Brand[3])
# for i in Brand:
    # print(i)

student1 = ["Yiğit", "Bilgi", 2010, [70,80,90]]
student2 = ["Ada", "Bilgi", 2011, [70,70,80]]
student3 = ["Çınar", "Turan", 2017, [60,60,90]]

Year = 2025
AgeForYigit = Year - student1[2]
print("Yiğitin Yaşi = " + str(AgeForYigit))
AgeForAda = Year - student2[2]
print("Adanın Yaşi = " + str(AgeForAda))
AgeForCinar = Year - student3[2]
print("Çınarın Yaşi = " + str(AgeForCinar))

ortalama1 = (student3[3][1] + student3[3][2] + student3[3][0]) / 3
print(ortalama1)





