def test():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
    yield 6

res = test()
print(res.__next__())
print(res.__next__())
print(res.__next__())