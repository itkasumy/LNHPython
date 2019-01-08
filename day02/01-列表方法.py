# string01 = "hello"
# print(string01)
# li01 = list(string01)
# print(li01, type(li01))
#
# string02 = str(li01)
# print(string02, type(string02))
#
# string03 = "".join(li01)
# print(string03)

li02 = [11, 22, 33, 44]
res01 = li02.append(55)
print(res01)
print(li02)

li02.clear()
print(li02)

li03 = [1, 2, 3, 4, 5]
li04 = li03.copy()
print(li04)

c = li03.count(1)
print(c)

li05 = [6, 7, 8]
li03.extend(li05)
print(li03)
li03.extend("我爱你亲爱的姑娘想到你就心里慌张")
print(li03)

i = li03.index("你")
print(i)

li06 = [11, 22, 33, 44]
val = li06.pop()
print(li06)
print(val)

li06.remove(22)
print(li06)

li06.reverse()
print(li06)

li07 = [11, 22, 33, 22, 44]
print(li07)
li07.sort()
print(li07)
li07.sort(reverse=True)
print(li07)
