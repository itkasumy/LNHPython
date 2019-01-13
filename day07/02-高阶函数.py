import time

# def foo():
#     time.sleep(.2)
#     print('hello ksm')
#
# def test(func):
#     start_time = time.time()
#     func()
#     stop_time = time.time()
#     print('函数的运行时间是:%s' %(stop_time - start_time))
#
# test(foo)


# def foo():
#     print('hello ksm')
#
# def test(func):
#     return func
#
# foo = test(foo)
# foo()


def foo():
    time.sleep(.3)
    print('来自foo')

def timer(func):
    start_time = time.time()
    func()
    end_time = time.time()
    print('函数的运行时间是:%s' %(end_time - start_time))

    return func

foo = timer(foo)
foo()