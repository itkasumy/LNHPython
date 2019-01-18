import random

print(random.random())

print(random.randint(1, 3))

print(random.randrange(1, 3))

print(random.choice([11, 22, 33]))

print(random.sample([11, 22, 33, 44, 55, 66], 2))

print(random.uniform(1, 3))

arr = [1, 2, 3, 4, 5]
random.shuffle(arr)
print(arr)

def v_code():
    res = ''
    string = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(5):
        num = random.randint(0, 9)
        alf = string[random.randint(0, 45)]
        res += str(random.choice([num, alf]))

    return res

print(v_code())