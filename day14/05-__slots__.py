class Foo:
    # __slots__ = ['name', 'age']
    __slots__ = 'name'

fi = Foo()
# print(fi.__dict__)
print(fi.__slots__)
fi.name = 'ly'
print(fi.name)

# fi.age = 18 => setattr => fi.__dict__['age'] = 18
# print(fi.age)