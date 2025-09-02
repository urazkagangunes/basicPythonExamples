# 1. Soru
# def printer(text, counter):
#     i = 0
#     while(i <= counter):
#         print(text)
#         i += 1

# printer("Ich liebe dich", 7)

# 2. Soru
# def calculateRectangle(wanted, a, b):
#     # wanted = input("Dikdörtgenin alanını hesaplamak istiyorsanız 'A' Çevresini hesaplamak isstiyrosanız 'Ç' yazınız. ")
#     if(wanted == 'A'):
#         return a * b
#     elif(wanted == 'Ç'):
#         return  2 * (a + b)
#     else:
#         return "Girilen harfi tekrar kontrol ediniz."

# print(calculateRectangle('Ç', 10, 7))

# 3. Soru
# def flipFlop():
#     import random
#     num = random.random()
#     if num > 0.5:
#         return "Tura"
#     else:
#         return "Yazı"
# print(flipFlop())

# 4. Soru
# def asalMi(a, b):
#     for num in range (a, b+1):
#         if(num > 1):
#             for i in range(2, int(num/2)):
#                 if(num % i == 0):
#                     break
#             else:
#                 print(num)
# asalMi(10, 20)

def tamBolenleriBul(num):
    tamBolenler = []

    for i in range(2, num):
        if(num % i == 0):
            tamBolenler.append(i)
    return tamBolenler

print(tamBolenleriBul(38))