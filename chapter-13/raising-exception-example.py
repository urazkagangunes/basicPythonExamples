# num = int(input("faktöriyelini hesaplamak istediğiniz sayıyı giriniz: "))
# total = 1 
# temp = 0
# if num > 0:
#     def fakt(num):
#         try:
#             total = 1
#             for i in range(1, num + 1):
#                 total *= i   
#             return total             
#         except:
#             pass
        
# else:
#     raise Exception("Num sıfırdan büyük olmak zorundadır.")

# print(f"{num} sayısının faktöriyeli: {fakt(num)}")


parola = input("Parolanızı giriniz: ")
def parolaKontrol(parola):
    turkce_karakterler = "şçğüöıİ"
    for i in parola:
        if i in turkce_karakterler:
            raise TypeError("Parola türkçe karakterler içeremez.")
    print("geçerli parola.")

try:
    parolaKontrol(parola)
except TypeError as e:
    print(e)