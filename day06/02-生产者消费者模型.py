# def producer():
# #     res = []
# #     for i in range(10000):
# #         res.append('包子%s' %i)
# #
# #     return res
# #
# # def consumer(res):
# #     for i, item in enumerate(res):
# #         print('第%s个人，%s' %(i, item))
# #
# # res = producer()
# # consumer(res)


# def test():
#     print('开始啦...')
#     first = yield 1
#     print('第一次', first)
#     yield 2
#     print('第二次')
#
# ts = test()
# res = ts.__next__()
# print(res)
# re = ts.send(None)
# print(re)


import time

def consumer(name):
    print('我是[%s],我准备开始吃包子了...' %name)
    while True:
        fd = yield
        time.sleep(.6)
        print('%s 很开心的把 %s 吃了...' %(name, fd))

def producer():
    cus1 = consumer('ksm')
    cus2 = consumer('xml')
    cus1.__next__()
    cus2.__next__()
    for i in range(10):
        time.sleep(1)
        cus2.send('槐花肉包%d' %i)
        cus1.send('槐花肉包%d' %i)

producer()
