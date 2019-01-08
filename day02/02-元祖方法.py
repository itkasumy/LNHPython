# list
li01 = [11, 22, 33, 44]
# tuple
tu01 = (11, 22, 33, 44)
print(tu01[0])
print(tu01[0:2])

for item in tu01:
    print(item)

string01 = "ksm"
tu02 = tuple(string01)
print(tu02)
li01.extend(tu02)
print(li01)

print(tu02.count('s'))
print(tu02.index('k'))
