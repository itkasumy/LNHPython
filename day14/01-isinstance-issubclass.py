class Foo:
    pass

class Bar(Foo):
    pass

obj = Foo()
print(isinstance(obj, Foo))
print(isinstance(obj, Bar))
print(isinstance(obj, object))

bar = Bar()
print(isinstance(bar, Bar))
print(isinstance(bar, Foo))
print(isinstance(bar, object))

print(issubclass(Bar, Foo))
print(issubclass(Bar, object))

