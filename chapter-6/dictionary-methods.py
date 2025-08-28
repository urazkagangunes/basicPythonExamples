food = {
    'foodName': 'Şambali',
    'Receipe': 'ŞambaliŞambali',
    'foodPic': '1.jpeg' 
}

#accessİtems

result = food['foodName']
result = food.get("foodName")
result = food.keys()
result = food.values()
result = food.items()

#updateİtems

food["foodName"] = "Çiğköfte"
food.update({"foodName": "Şuşi"})
food.update({"foodName2": "Çiğ Balık"})

#delete items

food.pop("foodName")
food.popitem()
food.clear()

result = food
print(result)