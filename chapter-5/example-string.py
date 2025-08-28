title = "Python ile Programlama Dersleri"

print(len(title))
print(title[0:6])
print(title[:6])
print(title[26:])
print(title[::-1])

name = input("Ad Soyad: ")
firstExamResult = int(input("Birinci sınav sonucunu giriniz: "))
secondExamResult = int(input("İkinci sınav sonucunu giriniz: "))
avgExamResult = float((firstExamResult + secondExamResult) / 2)

msg = f"{name} isimli öğrencinin 1.notu {firstExamResult}, 2.notu {secondExamResult} ve not ortalaması {avgExamResult} olarak hesaplanmıştır."
print(msg)