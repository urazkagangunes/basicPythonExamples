meyveler = {"elma", "aarmut", "şeftali", "elma"}
meyveler2 = {"elma", "aarmut", "şeftali", "kavun"}

# sonuc = meyveler[0]

# for i in meyveler:
#     print(i)

sonuc = "elma" in meyveler

meyveler.add("karpuz")
meyveler.update(meyveler2)
meyveler.remove("elma")
meyveler.discard("aarmut")
meyveler.pop()
meyveler.clear()
sonuc = meyveler
print(sonuc)