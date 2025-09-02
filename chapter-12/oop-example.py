class BankaHesabi:
    def __init__(self, hesapSahibi, bakiye):
        self.hesapSahibi = hesapSahibi
        self.bakiye = bakiye

    def paraYatir(self, yatirilacakParaMiktarı):
        #yatirilacakParaMiktarı = int(input("Yatırılacak tutarı giriniz: "))
        self.bakiye += yatirilacakParaMiktarı
        return f"Güncel bakiyeniz: {self.bakiye}"
    
    def paraCek(self, cekilecekTutar):
        #cekilecekTutar = int(input("Çekilmek istenen tutarı giriniz: "))
        if(self.bakiye >= cekilecekTutar):
            self.bakiye -= cekilecekTutar
            return f"Güncel bakiyeniz: {self.bakiye}"
        else:
            return f"Hesabınızda yeteri kadar para bulunmamaktadır. {self.bakiye}"
        
hesap1 = BankaHesabi("Uraz Kağan GÜNEŞ", 0)
hesap2 = BankaHesabi("Uraz GÜNEŞ", 0)
hesap3 = BankaHesabi("Kağan GÜNEŞ", 0)

hesaplar = [hesap1, hesap2, hesap3]

hesap1.paraYatir(1000)
print(hesap1.paraCek(2000)) 

for i in hesaplar:
    print(f"{i.hesapSahibi}'ındaki para miktarı: {i.bakiye}")