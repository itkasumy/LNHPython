class Foo:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        self.n += 1
        return self.n

fi = Foo(1)
print(fi.__next__())
print(fi.__next__())
print(fi.__next__())
print(fi.__next__())
print(fi.__next__())

for i in fi:
    print(i)

