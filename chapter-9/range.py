# for i in range (1, 100, 2):
#     print(i)

rng = range(10)
print(rng)
rng = range(10,20)
print(rng)
rng = range(100, 200, 10)
print(rng)
rng = range(0, -10, -1)
print(rng)
result = list(rng)
print(result)

for i in range(50, 250):
    if(i % 2 == 0):
        print(i)