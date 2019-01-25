def deco(obj):
    print('-' * 36)
    obj.x = 1
    obj.y = 2
    obj.z = 3
    return obj

# @deco
# def test():
#     print('test函数执行了...')
#
# test()

@deco
class Foo:
    pass

print(Foo.__dict__)
fi = Foo()
print(fi)
print(fi.x)
print(fi.y)
print(fi.z)