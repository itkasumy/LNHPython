# class Foo:
#     @property
#     def func(self):
#         print('get的时候运行')
#
#     @func.setter
#     def func(self, val):
#         print('**set的时候运行**', val)
#
#     @func.deleter
#     def func(self):
#         print('--def的时候运行--')
#
# fi = Foo()
# fi.func
# fi.func = 'abcdef'
# del fi.func



class Foo:
    def get_func(self):
        print('get的时候运行')

    def set_func(self, val):
        print('**set的时候运行**', val)

    def del_func(self):
        print('--def的时候运行--')

    func = property(get_func, set_func, del_func)

fi = Foo()
fi.func
fi.func = 'abcdef'
del fi.func