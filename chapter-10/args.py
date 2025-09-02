# numbers = (10, 20, 30, 40 ,50)
# def sum(liste):
#     result = 0
#     for i in liste:
#         result += i
#     return result

# def sum(*args):
#     print(args)
#     print(type(args))
#     result = 0
#     for i in args:
#         result += i

#     return result

# # result = sum(10, 20)
# result = sum(10, 20, 30, 40)
# print(result)


## kargs

def displayUser(**kwargs):
    print(type(kwargs))
    print(kwargs)

    for key, value in kwargs.items():
        print(f"{key}: {value}")
    print("\n")

displayUser(username="urazgunes")
displayUser(username = "urazkagan", email="uraazhunes@gmai.om")

def myFunc(a,b,c,*args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

myFunc(10, 20, 30, 40, 50, 60, 70, key1="value1", key2="value2")