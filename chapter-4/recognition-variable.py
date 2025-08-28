# 2000 + 2000 * %18

productAPrice = 2000
productBPrice = 3000
rate = 0.18

print(productAPrice + (productAPrice * rate)) # ürün A
print(productBPrice + (productBPrice * rate)) # ürün B

productSum = productBPrice + productAPrice
#print("Ürünlerin Toplam Değeri: " str(productSum + (productSum * rate)))
print(f"Ürünlerin Toplam Değeri: {productSum + (productSum * rate)}")
