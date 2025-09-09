import module

sonuc = module.sayi
sonuc = module.sayilar
sonuc = module.urun["urunAdi"]
sonuc = module.urun["renkler"]
sonuc = module.toplama(5,10)

import module as m
sonuc = m.sayi

from module import sayi, sayilar, urun
sonuc = sayi
sonuc = sayilar
sonuc = urun

from module import * #everything
sonuc = urun
sonuc = toplama(19,25)

print(sonuc)