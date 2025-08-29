# for => list, while => koşullu

numbers = [1,3,4,55,6,65,7676768,867,32]
names = ["Uraz", "Kağan", "GÜNEŞ", "Merve", "Nur"]
name = "Uraz Kağan GÜNEŞ"
# for i in numbers:
#     print(i)


for i in numbers:
    print("Hi")

for i in names:
    print(i)

for i in name:
    print(i)

my_tuple = [(1,2),(3,4),(5,6)]
for i,j in my_tuple:
    print(i,j)

my_dict = {
    "40": "Kırşehir",
    "34": "İstanbul",
    "16": "Bursa"
}

for i in my_dict.values():
    print(i)

    
for i in my_dict.keys():
    print(i)

    
for i, j in my_dict.items():
    print(i, j)