kurum = "BTK AKADMEİ".split() #str to list

print(type(kurum))
print(kurum)
print(kurum[0])
print(kurum[1])

sayilar= [1,2,3,4,5]
isimler = ["ali", "mehmet", "ayşe"]

print(type(isimler))
print(type(isimler[0]))

print(type(sayilar))
print(type(sayilar[0]))

student = ["Çınar", "Turan", 60,70,80]

print(student[0] + " "+ student[1])
ortalama = (student[2] + student[3] + student[4]) / 3
print(ortalama)

students = [["uraz", "güneş", 70,70,70], ["Ali", "Turan", 50,60,70]]

print(students[0][1])
print(students[1][0])