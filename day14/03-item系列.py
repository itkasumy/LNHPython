class Foo:
    def __getitem__(self, item):
        print('getitem')
        return self.__dict__[item]
    def __setitem__(self, key, value):
        print('setitem')
        self.__dict__[key] = value
    def __delitem__(self, key):
        print('delitem')
        self.__dict__.pop(key)

fi = Foo()
print(fi.__dict__)

fi['name'] = 'ksm'
print(fi.__dict__)
fi['age'] = 18

# del fi.age
# print(fi.__dict__)

del fi['age']

print(fi['name'])

