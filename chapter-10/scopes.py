# local scope
# global scope

# x = "gloabal scope"

# def my_func():
#     x = "local scope"
#     print(x)

# my_func()
# print(x)

# name = "Uraz"

# def change_name(new_name):
#     name = new_name
#     print(name)

# change_name("Kağan")
# print(name)

# name = "global"
# def greeting():
#     name = "uraz"

#     def hello():
#         name = "Kağan" 
#         print("hello", name)
    
#     hello()

# greeting()


x = 50

def test():
    global x
    print(f"x: {x}")

    x = 100
    print(f"changed x to {x}")

test()
print(x)