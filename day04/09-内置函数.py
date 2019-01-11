# # 绝对值
# print(abs(-1))
#
# # all()
# print(all([1, 2, 'a']))
# print(all([1, 2, 'a', '']))
#
# # any()
# print(any(['', 0]))
# print(any(['', '0']))
#
# # bin()
# print(bin(3))
#
# # hex()
# print(hex(123))
#
# # oct()
# print(oct(123))
#
# # bool()
# print(bool(8))
#
# # bytes()
# print(bytes('宗', encoding='utf-8'))
# print(bytes('宗', encoding='utf-8').decode(encoding='utf-8'))
#
# # chr()
# print(chr(10000))
#
# # dir()
# print(dir(all))
#
# # divmod()
# print(divmod(10, 3))
#
# # eval()
# dict_str = "{'name': 'ksm'}"
# print(eval(dict_str))
# calc_str = '1 + 2 * (4 / 2)'
# print(eval(calc_str))
#
# # hash()
# print(hash('3245345678kl'))
# print(hash('3245345678kl'))
# print(hash('3245345678kl'))
# print(hash('3245345678kl '))
#
# # help()
# print(help(all))
#
# # isinstance()
# print(isinstance(1, int))
# print(isinstance(1, bool))
# print(isinstance(True, bool))
# print(isinstance(1, bool))
#
# # globals()
# a = 1
# print(globals())
#
# # locals()
#
# nums = [1, 5, 3, 5, 0, 3]
# print(max(nums))
# print(min(nums))

# zip()
# print(list(zip(('a', 'b', 'c'), (1, 2, 3))))
#
# person = {'name': 'ksm', 'age': 18, 'gender': 'boy'}
# print(list(zip(person.keys(), person.values())))
#
# print(list(zip('hello', '12345')))
#
# scores = {'math': 98, 'chinese': 66, 'english': 99, 'history': 86}
# print(max(zip(scores.values(), scores.keys())))

# ord()
# print(ord('c'))

# pow()
# print(pow(2, 3))
# print(pow(2, 3, 3)) # 结果取余

# reversed()
# arr = [1, 3, 4, 6]
# print(list(reversed(arr)))

# round()
# print(round(3.5))

# set()
# print(set('hello'))

# slice()
# s1 = slice(3, 5)
# s2 = slice(1, 4, 2)
# string = 'hello'
# print(string[s1])
# print(string[s2])
# print(s2.start)
# print(s2.stop)
# print(s2.step)

# stu_info_list = [
#     {'name': 'zhangsan', 'age': 18},
#     {'name': 'lisi', 'age': 24},
#     {'name': 'wangwu', 'age': 17},
#     {'name': 'zhaoliu', 'age': 22},
# ]
#
# print(sorted(stu_info_list, key=lambda stu: stu['age']))

# sum()
# arr = [1, 2, 3, 4, 5, 6]
# print(sum(arr))

# vars()
# def test():
#     msg = 'laeuodsnvcl'
#     print(locals())
#     print(vars())
#
# test()
# print(vars(int))

# __import__()
module_name = 'test'
test = __import__(module_name)
test.sayHi()
