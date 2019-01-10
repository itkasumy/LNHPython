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

nums = [1, 5, 3, 5, 0, 3]
print(max(nums))
print(min(nums))