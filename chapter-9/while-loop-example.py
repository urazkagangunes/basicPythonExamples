# 1. soru

# number1 = int(input('Birinci sayıyı ver: '))
# number2 = int(input('İkinci sayıyı ver: '))

# start = min(number1, number2)
# end = max(number1, number2)

# while (start <= end):
#     if(start % 2 == 0):
#         print(start)
#     start += 1

# 2.Soru

# i = 100
# while (i > 0):
#     print(i)
#     i -= 1

# 3. Soru

# i = 0
# numbers = []

# while (i <= 4):
#     num = int(input(f'{i+1}. sayı: '))
#     numbers.append(num)
#     i += 1

# numbers.sort()
# print(numbers)

# 4. Soru

# username = ''
# while not username:
#     username = input('username giriniz')
#     print(username)


# 5. Soru

n = int(input('kaç adet öğrenci bilgisi girmek istersiniz? '))
studentDict = {}
while (n > 0):
    studentNo = int(input('Öğrenci numarasını giriniz: '))
    studentName = input('Öğrenci adını giriniz: ')
    studentLastName = input('Öğrenci soyad giriniz: ')
    studentDict[studentNo] = {
            'student_name': studentName,
            'student_lastname': studentLastName
        }
    n -= 1
print(studentDict)