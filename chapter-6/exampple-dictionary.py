students = {
    101: {
        'fullName': 'Uraz Kağan GÜNEŞ',
        'birthYear': 2010,
        'notes' : [40, 80, 90]
    },
    102: {
        'fullName': 'Uraz GÜNEŞ',
        'birthYear': 2012,
        'notes' : [80, 80, 80]
    },
    103: {
        'fullName': 'Kağan GÜNEŞ',
        'birthYear': 2017,
        'notes' : [70, 70, 70]
    }
}

schoolNumber = int(input('Öğrenci numaranızı giriniz: '))
print(f"{schoolNumber} numaralı {students[schoolNumber]['fullName']} isimli öğrencinin yaşı {2025 - students[schoolNumber]['birthYear']} ve not ortalaması {sum(students[schoolNumber]['notes']) / len(students[schoolNumber]['notes'])}")