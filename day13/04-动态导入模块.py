# from module import test

# module_test = __import__('module.test')
# print(module_test)
#
# module_test.test.demo()
# module_test.test._dm()


# from module.test import *
#
# demo()
# # _dm()

# from module.test import demo, _dm
# demo()
# _dm()


import importlib
test = importlib.import_module('module.test')
print(test)
test.demo()

module_test = __import__('module.test')
print(module_test)
module_test.test.demo()