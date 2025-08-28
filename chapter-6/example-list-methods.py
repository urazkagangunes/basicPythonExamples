customers = ["urazgunes", "mervedurmus", "kagangunes", "nurdurmus"]
order_totals = [12000, 13000, 5000, 15000]

#ekleme
customers.append("urazgunes")
order_totals.append(5000)

#silme
customers.pop(-1)
order_totals.pop(-1)
sonuc = customers
sonuc = order_totals

# for i, name in enumerate(customers):
#     print(f"{name} isimli müşterinin sipariş toplamı {order_totals[i]}")

customers.sort()
sonuc = customers

order_totals.sort()
order_totals.reverse()
sonuc = order_totals

# order_totals.min()
sonuc = min(order_totals)

sonuc = customers.count("urazgunes")

# customers.remove("nurdurmus")
# sonuc = customers

# customers.clear()
# sonuc = customers

username = input('customer name: ')
total_price = input('how much money do you spend? ')
customers.append(username)
order_totals.append(total_price)

print(customers)
print(order_totals)
