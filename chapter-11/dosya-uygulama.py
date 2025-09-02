def notGir():
    ad = input("Öğrencinin adını giriniz:\n")
    soyad = input("Öğrencinin soyadını giriniz:\n")
    not1 = input("Öğrencinin birinci notunu giriniz:\n")
    not2 = input("Öğrencinin ikinci notunu giriniz:\n")
    not3 = input("Öğrencinin üçüncü notunu giriniz:\n")

    with open("sinav_notlari.txt", "a", encoding='utf-8') as file:
        file.write(ad + ' ' + soyad + ':' + not1 + ',' + not2 + ',' + not3 + '\n')

def notOku():
    with open("sinav_notlari.txt", "r", encoding='utf-8') as file:
        for i in file:
            print(i)

def notHesapla(i):
    i = i[:-1]
    liste = i.split(":")

    ogrenciAdı = liste[0]
    notlar = liste[1].split(',')

    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])

    ortalama = (not1 + not2 + not3) / 3

    if(ortalama >= 90 and ortalama <= 100):
        harf = "AA"
    elif(ortalama >= 80 and ortalama <= 89):
        harf = "BA"
    elif(ortalama >= 75 and ortalama <= 79):
        harf = "BB"
    elif(ortalama >= 70 and ortalama <= 74):
        harf = "CB"
    elif(ortalama >= 65 and ortalama <= 69):
        harf = "CC"
    elif(ortalama >= 60 and ortalama <= 64):
        harf = "DC"
    elif(ortalama >= 50 and ortalama <= 59):
        harf = "DD"
    elif(ortalama >= 40 and ortalama <= 49):
        harf = "FD"
    elif(ortalama >= 0 and ortalama <= 39):
        harf = "FF"

    return f"{ogrenciAdı} : {harf} - ({ortalama})\n"

def notKayit():
    with open("sinav_notlari.txt", "r", encoding='utf-8') as file:
        liste = []
    
        for satir in file:
            liste.append(notHesapla(satir))
    
        with open("sonuclar.txt", "w", encoding='utf-8') as file2:
            file2.writelines(liste)

while True:
    islem = input("1-Not Gir.\n2-Notları Oku.\n3-Notları Kayıt Et.\n4-Çıkış\nSeçiminiz?\n")

    if(islem == "1"):
        notGir()
    elif(islem == "2"):
        notOku()
    elif(islem == "3"):
        notKayit()
    else:
        break