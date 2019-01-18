import time

print(time.time())

print(time.localtime())
t = time.localtime()
print(t.tm_yday)
print(t.tm_wday)

print(time.gmtime())

# 时间戳转结构化时间
print(time.localtime(1234567890))
print(time.gmtime(1234567890))

# 结构化时间转时间戳
print(time.mktime(time.localtime()))

# 将结构化时间转格式化时间
print(time.strftime('%Y-%m-%d %X', time.localtime()))

# 将格式化时间转结构化时间
print(time.strptime('2019-01-18 14:13:45', '%Y-%m-%d %X'))



print(time.asctime())
print(time.ctime())

import datetime
print(datetime.datetime.now())