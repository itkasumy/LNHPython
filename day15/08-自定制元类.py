class MyType(type):
    def __init__(self, name, instance, dic):
        print('元类的构造函数执行...')
        print(name)
        print(instance)
        print(dic)

class Foo(metaclass=MyType):
    def __init__(self, name):
        self.name = name

fi = Foo('ksm')
print('-' * 36)
print(fi.__dict__)