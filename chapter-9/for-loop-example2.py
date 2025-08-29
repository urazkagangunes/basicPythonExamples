products = [
    {"productName":"HP Victus", "Price":32999},
    {"productName":"Lenova ThinkPad", "Price":25499},
    {"productName":"Apple Macbook", "Price":49999},
    {"productName":"Huawei Matebook", "Price":26999},
    {"productName":"Casper Nirvana", "Price":20000},
]

# soru 1
# for i in products:
#     print(f"{i['productName']} marka ürünün fiyatı {i['Price']}₺.")

# # soru 2
# sum = 0

# for i in products:
#     sum += i['Price']

# print(sum)

# soru 3
# for i in products:
#     if((i['Price'] >= 25000) and (i['Price'] <= 40000)):
#         print(i['productName'])

# soru 4
wonder = input("Hangi ürün hakkında bilgi almak istiyorsunuz? ")

for i in products:
    if(wonder == i['productName']):
        print(f"{i['productName']} marka ürünün fiyatı {i['Price']}₺.")
else:
    print("aradığınız ürün bulunamadı.")