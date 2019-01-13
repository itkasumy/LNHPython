import time

# def calc(arr):
#     res = 0
#     start_time = time.time()
#     for i in arr:
#         res += i
#         time.sleep(.1)
#
#     end_time = time.time()
#     print('函数的运行时间是：%s' %(end_time - start_time))
#     return res
#
# print(calc(range(100)))

# 装饰器 = 高阶函数 + 函数嵌套 + 闭包

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        stop_time = time.time()
        print('函数运行的时间是%s' %(stop_time - start_time))
        return res

    return wrapper

@timer

def calc(arr):
    res = 0
    for i in arr:
        time.sleep(.1)
        res += i

    return res

print(calc(range(20)))