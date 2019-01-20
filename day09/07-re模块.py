import re

ret = re.findall('k.m', 'kljadoksmdhkkmkmm')
print(ret)

ret = re.findall('^k..', 'kljadoksmdhkkmkmm')
print(ret)

ret = re.findall('k.m$', 'kljadoksmdhkkmkmm')
print(ret)
