# module1 (db) : urunler
# module2 (methods) : urunEkle(), urunGüncelle(), urunleriGetir()
# module3 (app) :

#         yeni ürün ekleme => urunEkle("iphone 15", 60000)
#         ürün güncelle    => urunGüncelle(1, "iphone 15 pro", 80000)
#         ürünleri listele => ürünleriGetir()

import module2 as m2
# m2.addProduct()
# m2.updateProduct()
m2.listProduct()

