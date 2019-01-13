# a, b, c = 'hel'
# print(a)
# print(b)
# print(c)
#
# a, b, c = (1, 3, 5)
# print(a)
# print(b)
# print(c)

ls = [1, 2, 3, 4, 5, 6, 7]
# a, *_, b = ls
# print(a)
# print(b)

_, a, *_, b, _ = ls
print(a)
print(b)

a = 1
b = 2
a, b = b, a
print(a, b)