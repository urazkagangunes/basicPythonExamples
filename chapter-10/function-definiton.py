# def greetings():
#     for i in range(7):
#         print("Hi everyone!")
# greetings()


# a = int(input('sayı: '))
# b = int(input('sayı: '))
# def sum(a, b):
#     print(a + b)
# sum(a, b)

# def sum():
#     return 7 + 7

# result = sum()

# def year():
#     import datetime
#     return datetime.datetime.now().year

# def hour():
#     import datetime
#     return datetime.datetime.now().hour
# def calculateTheAge():
#     return year() - 1999
# print(calculateTheAge())

# def greeting2():
#     if(hour() < 12):
#         return "GÜNO"
#     else:
#         return "Halo"
# print(greeting2())

# def greet(name):
#     return "Halo " + name
# print(greet("Uraz"))

# def sum(num1, num2):
#     return num1 + num2
# print(sum(7, 13))

def calculateAge(bDate):
    return 2025 - bDate
print(calculateAge(1999))

def retirementYear(bDate, name):
    age = calculateAge(bDate)
    leftDays = 65 - age

    if(leftDays > 0):
        return f"{name} emekliliğinize {leftDays} yıl kaldı."
    else:
        return f"{name} zaten {abs(leftDays)} yıl önce emekli oldunuz"

print(retirementYear(1800, "Uraz"))
