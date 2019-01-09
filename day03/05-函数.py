def test(x):
    '''
    计算2n + 1
    :param x:
    :return:
    '''
    return x * 2 + 1

print(test(3))

def calc(x, y):
    return x ** y

print(calc(2, 3))
print(calc(3, 2))

def test2(x, *args):
    print(x)
    print(args)

test2(1, 2, 3, 4, 5, 6, 5)

def test3(x, **kwargs):
    print(x)
    print(kwargs)

test3(1, w=1, y=2, z=3)

def test4(x, *args, **kwargs):
    print(x)
    print(args)
    print(kwargs)

test4(1, 2, 3, 4, 5, 6, 4, 5, 3, y='ksm', z='wlm', w='xml', m=6, n=7)
