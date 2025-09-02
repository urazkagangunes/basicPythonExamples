f = open("log.txt", encoding='utf-8')

f.seek(0) # cursoru sıfırlar
print(f.readline()) #satır
print(f.readlines()) # liste halinde geitiri
print(f.read()) # okur
f.close #dosyayı kapatır tekrar f.open yapmak zorundasın