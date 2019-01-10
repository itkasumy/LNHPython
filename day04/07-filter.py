nums = [1, 2, 3, 5, 7, 9, 4, 6]

# def filter_test(arr):
#     res = []
#     for i in arr:
#         if not i % 2 == 0:
#             res.append(i)
#
#     return res
#
# print(filter_test(nums))

def isOdd(i):
    return i % 2 != 0

def filter_test(arr, fun):
    res = []
    for i in arr:
        if fun(i):
            res.append(i)

    return res

print(filter_test(nums, isOdd))

print(filter_test(nums, lambda n: n % 2 != 0))

print(list(filter(lambda n: n % 2 != 0, nums)))