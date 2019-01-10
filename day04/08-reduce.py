from functools import reduce

nums = [1, 2, 3, 4, 5, 6]

# def reduce_test(arr):
#     res = 0
#     for i in arr:
#         res += i
#
#     return res
#
# print(reduce_test(nums))

def reduce_test(fun, arr, init=None):
    if init is None:
        res = arr.pop(0)
    else:
        res = init
    for i in arr:
        res = fun(res, i)

    return res

print(reduce_test(lambda m, n: m + n, nums))

print(reduce_test(lambda m, n: m * n, nums))

print(reduce(lambda m, n: m + n, nums, 0))

print(reduce(lambda m, n: m * n, nums, 1))
