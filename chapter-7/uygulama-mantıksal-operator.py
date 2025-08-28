# soru 1
# age = int(input('yasını gir: '))
# permission = (input('izin var mı yok mu? '))

# result = (age >= 18) or (permission == 'var')
# print(result)

# soru 2
# grade = int(input('ders notun kaç? '))

# result = (grade >= 50)

# print(result)

# soru 3
# grade = int(input('ders notun kaç? '))
# fail = input('herhangi bir dersten kaldın mı? E/H')

# result = (grade >= 70) and (fail == 'H')
# print(f"Teşekkür alabilme durumu: {result}")

# soru 4
# graduate = input('mezuniyet dereceniz: ')
# smoke = input('sigara kullanıyor musunuz? ')

# result = (graduate == 'önlisans' or graduate == 'lisans') and (smoke == 'Hayır')
# print(result)

# soru 5
username = input('kullanıcı adınızı giriniz: ')
email = input('email adresinizi giriniz: ')
password = int(input('şifrenizi giriniz: '))

result = (username == 'urazgunes' or email == 'urazkagangunes@gmail.com') and (password == 1234567)
print(f"Giriş başarılı mı? {result}")