numbers = [3, 5, 7, 2, 12, 32, 45]

# 1.soru
# for i in numbers:
#     print(i)

# 2.soru
# for i in numbers:
#     if(i % 3 == 0):
#         print(i)

# 3.soru
# sum = 0
# for i in numbers:
#     sum = sum + i
# print(sum)

products = ["samsung s24", "samsung s22", "iphone 14", "iphone 7"]

# 4.soru
# for i in products:
#     if(i.startswith('iphone')):
#         print(i)

# 5.soru
total = 0
for i in products:
    total += i.count('samsung')
print(total)