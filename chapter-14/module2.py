import module1 as m1
def addProduct():
    productName = input("Yeni ürünün adını giriniz.")
    productPrice = int(input("Yeni ürünün fiyatını giriniz."))

    if m1.products:
        new_id = max(m1.products.keys()) + 1
    else:
        new_id = 1

    m1.products[new_id] = {
        "productName": productName,
        "price": productPrice
    }

    listProduct()

def updateProduct():
    productId = int(input("Güncellenecek ürünün ID'sini giriniz."))
    
    if(productId in m1.products):
        product = m1.products[productId]
        print(f"Mevcut ürün: {product['productName']} - {product['price']} TL")
    
    updatedName = input("Güncellenen adı giriniz.")
    product["productName"] = updatedName

    updatedPrice = int(input("Güncellenen yeni fiyatı giriniz."))
    product["price"] = updatedPrice

    m1.products[productId] = product
    
    listProduct()


def listProduct():
    if not m1.products:
        print("Ürün bulunamadı.")
        return
    
    print("===Ürün Listesi===")
    for pid, product in m1.products.items():
        print(f"ID: {pid} | {product['productName']} - {product['price']} ₺")
