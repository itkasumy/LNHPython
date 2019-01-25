class Fib:
    def __init__(self):
        self.a = 1
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a

fib = Fib()

print(fib.__next__())
print(fib.__next__())
print(fib.__next__())
print(fib.__next__())
print(fib.__next__())