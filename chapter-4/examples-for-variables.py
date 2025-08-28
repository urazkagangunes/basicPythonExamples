name = input("name: ")
cellPhoneNumber = input("cellPhoneNumber: ")
mail = input("Mail: ")
city = input("city: ")

wirelessMousePrice = 550
wirelessKeyboardPrice = 650
laptopPrice = 55000
rate = 0.18

totalPrice = (wirelessKeyboardPrice + wirelessMousePrice + laptopPrice) * rate

#print("Kullanıcı bilgileri: " '\n' + name '\n'+ cellPhoneNumber '\n'+ mail '\n'+ city '\n')
print("Kullanıcı bilgileri: " + '\n' + name + '\n' + cellPhoneNumber + '\n' + mail + '\n' + city + '\n')
print(f"Kullanıcının toplam masrafı: {totalPrice}")