string01 = 'I am {}, my age is {}, {}'.format('seven', 18, 'ksm')
print(string01)

string02 = 'I am {2}, my age is {1}, {0}'.format('seven', 18, 'ksm')
print(string02)

string03 = 'I am {1}, my age is {0}, {1}'.format(18, 'ksm')
print(string03)

string04 = 'I am {name}, my age is {age}, real name is {name}'.format(name='ksm', age=18)
print(string04)

string05 = 'I am {name}, my age is {age}, real name is {name}'.format(**{'name': 'ksm', 'age': 18})
print(string05)

string06 = 'I am {0[0]}, age {0[1]}, really {1[2]}'.format([1, 2, 3], [11, 22, 33])
print(string06)

string07 = 'I am {:s}, age {:d}, money {:f}'.format('ksm', 18, 999999999.99)
print(string07)

string08 = 'I am {:s}, age {:d}'.format(*['ksm', 18])
print(string08)

