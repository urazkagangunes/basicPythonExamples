# cities = ['kırşehir', 'bursa']
# plateNumber = [40, 16]

# print(plateNumber[0], cities[0])
# print(plateNumber[1], cities[1])

# print(plateNumber[cities.index('kırşehir')])
# print(plateNumber[cities.index('bursa')])


#dictionary

plateNumbers = {
    'Kırşehir': 40,
    'Bursa': 16,
    'İstanbul': 35
}

plateNumbers['İstanbul'] = 34

print(plateNumbers['İstanbul'])
print(plateNumbers['Kırşehir'])
print(plateNumbers['Bursa'])
