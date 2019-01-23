# class Foo:
#     x = 1
#     def __init__(self, y):
#         self.y = y
#
#     def __getattr__(self, item):
#         print('执行__getattr__')
#
#
# f = Foo(10)
# print(f.y)
# print(getattr(f, 'y'))
#
# f.abcdefghijklmn


# class Foo:
#     x = 1
#     def __init__(self, y):
#         self.y = y
#
#     def __delattr__(self, item):
#         print('执行__delattr__')
#
#
# f = Foo(10)
# del f.y
# del f.x


class Foo:
    x = 1
    def __init__(self, y):
        self.y = y

    def __setattr__(self, key, value):
        print('执行__setattr__')
        # self.key = value # 进入递归
        self.__dict__['key'] = value


f = Foo(10)
f.z = 2