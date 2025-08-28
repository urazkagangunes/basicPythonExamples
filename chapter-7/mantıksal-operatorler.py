age = int(input('yaşınızı giriniz: '))
graduate = input('mezuniyetinizi giriniz: ')

result = (age >= 18) and (graduate == 'lise' or graduate == 'üniversite')

print(result)