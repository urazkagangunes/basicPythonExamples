def fullName(firstName: str, lastname: str, age: int) -> str:
    return f"Your name is {firstName} {lastname}, {age} yaşdasınız."

result = fullName("Uraz", "GÜNEŞ", 23)
result = fullName(lastname="GÜNEŞ", firstName="Kağan", age=23)
result = fullName(firstName="uraz", lastname="kağan", age=23)

print(result)