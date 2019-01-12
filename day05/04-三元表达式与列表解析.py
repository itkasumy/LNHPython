# def fib(n):
#     return 1 if n == 1 or n == 2 else fib(n - 1) + fib(n - 2)
#
# print(fib(8))
#
# # 列表解析
# # egg_list = []
# # for i in range(10):
# #     egg_list.append('鸡蛋%s' %i)
# # egg_list = ['鸡蛋%s' %i for i in range(10)]
# egg_list = ['鸡蛋%s' %i for i in range(10) if i > 5]
#
# print(egg_list)

hen = ('鸡蛋%s' %i for i in range(10)) # 生成器表达式
print(hen)
print(hen.__next__())
print(hen.__next__())
print(next(hen))
print(next(hen))
