# liste = ["1", "3", "5", "20b", "abc", "10a", "60"]
# for i in liste:
#     try:
#         sonuc = int(i)
        # print(sonuc)
    # except Exception as e:
        # print(e)


# devamMi = ''
# while (devamMi != "q"):
#     try:
#         numero = int(input("sayı giriniz: "))
#     except Exception as e:
#         print(e)

#     devamMi = input("Çıkış yapmak istiyrsnız q ya basınız.")


urun = {"urunAdi":"samsung s20", "fiyat": 12313}

def get(liste,key):
    try:
        return liste[key]
    except KeyError:
        return None

sonuc = get(urun, "fiyat")
sonuc = get(urun, "sad")

print(sonuc)