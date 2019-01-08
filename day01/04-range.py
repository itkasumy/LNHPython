# v1 = range(100)
# for item in v1:
#     print(item)
#
# v2 = range(0, 100, 5)
# for item in v2:
#     print(item)

info = input(">>>")
print(info)

l = len(info)
count = range(l)
for item in count:
    print(item, info[item])
