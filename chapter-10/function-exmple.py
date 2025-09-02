# Bankamatik uygulaması

accounts = {
    101: {
        "tamAd": "Uraz Kağan GÜNEŞ",
        "dogumYili": 1999,
        "bakiye": 1000000
    },
    102: {
        "tamAd": "Kağan GÜNEŞ",
        "dogumYili": 1998,
        "bakiye": 0
    },
    103: {
        "tamAd": "Uraz GÜNEŞ",
        "dogumYili": 1997,
        "bakiye": 10000
    }
}

def menu():
    islem = int(input("Yapmak istediğiniz işlemi seçiniz: Para Yatırma: 1, Para Çekme: 2, Bakiye Sorgulama: 3"))
    if(islem == 2):
        cekilmekIstenenTutar = int(input("Çekilmek istenen tutarı giriniz: "))
        paraCekme(cekilmekIstenenTutar)
    elif(islem == 1):
        yatırılmakIstenenPara = int(input("Yatırmak istediğiniz miktarı giriniz: "))
        paraYatırma(yatırılmakIstenenPara)
    elif(islem == 3):
        bakiyeSorgula()
    else:
        print("Lütfen menüden doğru tuşlama yapınız...")

def paraCekme(cekilmekIstenenTutar):
    if (accounts[account]["bakiye"] < cekilmekIstenenTutar):
        print("Yetersiz Bakiye...")
    else:
        accounts[account]["bakiye"] -= cekilmekIstenenTutar
        print("Kalan bakiyeniz", accounts[account]["bakiye"])
        

def paraYatırma(yatırılmakIstenenPara):
    if(yatırılmakIstenenPara > 0):
        accounts[account]["bakiye"] += yatırılmakIstenenPara
        print("Yeni bakiyeniz" + accounts[account]["bakiye"])
    else:
        print("Yatırılmak istenen tutar 0 dan büyük olmalıdır.")

def bakiyeSorgula():
    print(f"GÜncel bakiye durumunuz: {accounts[account]["bakiye"]}")


bankaMatikDurum = 'D'
while(bankaMatikDurum == 'D'):
    account = int(input("İşlem yapmak istediğiniz banka numarasını giriniz..."))
    accounts[account]
    menu()
    bankaMatikDurum = input("İşleme devam etmek istiyorsanız 'D'ye basınız devam etmek istemiyprsanız herhangi bir tuşa basınız...")






