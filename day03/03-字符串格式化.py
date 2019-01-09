msg1 = 'My name is %s, I like %s' % ('ksm', 'cat')
print(msg1)

msg2 = 'persent %.2f%%' % 99.7497496
print(msg2)

msg3 = 'My name is %(name)s, my age is %(age)d' % {'name': 'ksm', 'age': 24}
print(msg3)

print('a', 'b', 'c', 'd', sep=':')
