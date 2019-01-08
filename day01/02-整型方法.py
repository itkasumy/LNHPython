a = "123"
print(a, type(a))

b = 123
print(b, type(b))

c = int(a)
print(c, type(c))

num1 = "0011"
v1 = int(num1, base=2)
v2 = int(num1, base=8)
v3 = int(num1, base=16)
print(v1, v2, v3)

num2 = "a"
v4 = int(num2, base=16)
print(v4)

age = 18
print(age.bit_length())