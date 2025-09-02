## ENUMARATE
# brands = ["opel", "bmw", "togg"]

# i = 1

# for brand in brands:
#     print(f"{i}-{brand}")
#     i += 1

# obj1 = enumerate(brands, 1)
# print(type(obj1))
# print(list(obj1))

# for i, brand in enumerate(brands, 1):
#     print(brand)

## ZİP
numbers = [100, 200, 300]
students = ["Uraz", "Kağan", "GÜNEŞ"]

print(list(zip(numbers, students)))

for num, student in zip(numbers, students):
    print(num, student)