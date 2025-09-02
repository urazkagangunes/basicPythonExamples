class Product:
    #attribute, property
    def __init__(self, name, price, isActive):
        self.name = name
        self.price = price
        self.isActive = isActive
    #instance method
    def get_product(self):
        return f"ürün adı. {prodcut.name} ürün fiyatı: {prodcut.price} kdv fiyat: {self.kdv_price()}"

    def kdv_price(self):
        return self.price * 1.20
    

p1 = Product("Iphone 15", 200000, True)
p2 = Product("Samsung S24", 332232, False)
p3 = Product("Iphone 14", 2123113, True)


products = [p1, p2, p3]

for prodcut in products:
    if prodcut.isActive:
        print(prodcut.get_product())