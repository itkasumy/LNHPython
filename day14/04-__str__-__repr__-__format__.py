# arr = list('hello')
# print(arr)

# class Foo:
#     pass
#
# foo = Foo()
# print(foo)

# class Foo:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def __str__(self):
#         return '自定制的对象显示:name=%s age=%s' %(self.name, self.age)
#
# foo = Foo('ksm', 24)
# print(foo)


# class Foo:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def __repr__(self): # 在解释器中运行
#         return '自定制的对象显示:name=%s age=%s' %(self.name, self.age)
#
# foo = Foo('ksm', 24)
# print(foo)


# string = '{0}{0}{0}'.format('fi')
# print(string)

# class Date:
# #     def __init__(self, year, month, day):
# #         self.year = year
# #         self.month = month
# #         self.day = day
# #
# # dt = Date(2019, 1, 24)
# # # string = '{0}{0}{0}'.format(dt)
# # # print(string)
# # string = '{0.year}{0.month}{0.day}'.format(dt)
# # print(string)

fmt_dic = {
    'ymd': '{0.year}{0.month}{0.day}',
    'y-m-d': '{0.year}-{0.month}-{0.day}',
    'y:m:d': '{0.year}:{0.month}:{0.day}',
}

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, format_spec):
        if not format_spec:
            format_spec = 'ymd'
        return fmt_dic[format_spec].format(self)

dt = Date(2019, 1, 24)
print(format(dt, 'ymd'))
print(format(dt, 'y-m-d'))
