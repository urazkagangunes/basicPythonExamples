# file = open("log.txt", encoding='utf-8')

# print(file.read())

# file.close()

try:
    with open("log2.txt", encoding='utf-8') as file:
    # print(file.read())
    # print(file.tell())
    # print(file.read())
    # print(file.tell())

        for i in file:
            print(i, end="")
except FileNotFoundError as e:
    print("Dosya Okuma Hatası.")