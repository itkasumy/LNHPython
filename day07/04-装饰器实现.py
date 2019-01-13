import time
# 装饰器框架
def timer(func):
    def wrapper():
        start_time = time.time()
        func()
        stop_time = time.time()
        print('函数运行的时间是:%s' %(stop_time - start_time))

    return wrapper

@timer

def test():
    time.sleep(.6)
    print('test函数运行完毕...')

# wrapper = timer(test)
# wrapper()

# test = timer(test)
# test()

'''
语法糖: @timer 就相当于 test = timer(test)
'''

test()
