class Foo:
    pass

fi = Foo()

print(type(fi))
print(type(Foo))

def __init__(self, x, y):
    self.x = x
    self.y = y

Bar = type('Foo', (object,), {'name': 'ksm', '__init__': __init__})
print(Foo)
print(Bar)

print(Foo.__dict__)
print(Bar.__dict__)

fii = Bar(1, 2)
print(fii.name)
print(fii.x)
print(fii.y)
