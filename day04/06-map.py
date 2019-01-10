nums = [1, 2, 10, 5, 3, 7]

# def map_test(arr):
#     ret = []
#     for i in arr:
#         ret.append(i ** 2)
#
#     return ret
#
# print(map_test(nums))

def add_one(i):
    return i + 1

def ping_fang(i):
    return i ** 2

def map_test(arr, fun):
    ret = []
    for i in arr:
        ret.append(fun(i))

    return ret

print(map_test(nums, ping_fang))

print(map_test(nums, lambda x: x ** 2))

# 用map处理
print(list(map(lambda x: x ** 2, nums)))

print(''.join(list(map(lambda l: l.upper(), 'hello world'))))
