import sqlite3

connection = sqlite3.connect("deneme.db")

cursor = connection.cursor()

sql = "INSERT INTO genres(name) VALUES('Macere')"
cursor.execute(sql)

connection.commit()

# cursor.execute("select * from customers where city='İStanulbu'")
# result = cursor.fetchall()
# result = cursor.fetchone()
# for i in result:
#     print(i[0] + " " + i[1])

connection.close()
print("veri tabanı bağlantısı hazır.")