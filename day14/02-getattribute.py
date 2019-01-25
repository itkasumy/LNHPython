# class Foo:
#     def __init__(self, x):
#         self.x = x
#
#     def __getattr__(self, item):
#         print('......')
#
#
# f = Foo(1)
# f.abcdef

class Foo:
    def __init__(self, x):
        self.x = x

    def __getattr__(self, item):
        print('......')

    def __getattribute__(self, item):
        print('******')


f = Foo(1)
print(f.x)
print(f.abcdef)

# raise AttributeError('属性异常')

