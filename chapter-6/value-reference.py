#value tyoes

# x = 10
# y = 20

# x = y 
# y = 30
# print (x,y)

# reference

a = ["elma", "armut"]
b = ["elma", "armut"]

a=b
a[0] = "üzüm"
print(a, b)

# liste kopyalama
listeA = [10, 20]
listeB = listeA
listeB = listeA.copy() # 1. yol
listeB = list(listeA) # 2.yol

listeB[0] = 30

print(listeB, listeA)