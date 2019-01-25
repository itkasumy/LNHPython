class Foo:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('执行了enter')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type)
        print(exc_val)
        print(exc_tb)
        print('执行了exit')
        # return True

with Foo('demo.txt') as fi:
    print(fi.name)
    print(abcdef)
    print('*' * 36)

print('-' * 42)
