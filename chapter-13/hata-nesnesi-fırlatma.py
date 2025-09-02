# x = 10

# if x > 5:
#     raise ValueError("x 5 den büyük olamöaz.")

def renklendir(text, renk):
    renkler = ("blue", "red", "white")
    if(type(text)) is not str:
        raise TypeError("renk str olmalıdır.")
    if(type(renk)) is not str:
        raise TypeError("renk str olmalıdır.")
    
    if renk not in renkler:
        raise ValueError("geçersiz renk.")
    
    print(f"{text} {renk} olarak yazıldı")

try:
    renklendir("as", "blue")
except (TypeError, ValueError) as ex:
    print(ex)