# def greet(name = {"Kim ooo"}, message = {"Alooo"}):
#     return f"{name} {message}"

# result = greet("Uraz", "Yemeeeek")
# print(result)

# def usAlma(taban, us = 2):
#     return taban ** us
# sonuc = usAlma(2, 3)
# sonuc = usAlma(5)


def toplam(a, b):
    return a + b

def cikarma(a, b):
    return a - b

def carpma(a, b):
    return a * b

def islem(a, b, fn=toplam):
    return fn(a, b)

sonuc = islem(10, 22, cikarma) 
print(sonuc)