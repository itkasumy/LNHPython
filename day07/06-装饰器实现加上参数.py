import time
# 装饰器框架
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        stop_time = time.time()
        print('函数运行的时间是:%s' %(stop_time - start_time))
        return res

    return wrapper

@timer

def test(name, age):
    time.sleep(.6)
    print('test函数运行完毕...,名字是【%s】,年龄是【%s】' %(name, age))
    return '这是test的返回值'

@timer

def test2(name, age, gender):
    time.sleep(.6)
    print('test2函数运行完毕...,名字是【%s】,年龄是【%s】,性别是【%s】' %(name, age, gender))
    return '这是test的返回值'

res = test('ksm', 18)
print(res)

res = test2('Jimmy', 24, 'male')
print(res)
