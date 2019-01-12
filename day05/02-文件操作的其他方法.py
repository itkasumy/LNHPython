# file = open('hexinlang', 'rb')
# # print(file.closed)
# # print(file.mode)
# # print(file.encoding)
# # file.flush() # 将内存中的数据保存到硬盘
# # print(file.name)
# print(file.tell())
# file.seek(0)
# print(file.tell())
# file.seek(10)
# print(file.tell())
# # seek() 0从文件开头，1从当前光标的位置，2从文件结尾
# file.seek(2, 1)
# print(file.tell())
# file.seek(-2, 2)
# print(file.tell())
# print(file.readline())

file = open('hexinlang', 'rb')

for i in file:
    offset = -10
    while True:
        file.seek(offset, 2)
        data = file.readlines()
        if len(data) > 1:
            print('文件的最后一行是:%s' %(data[-1].decode('utf8')))
            break
        offset *= 2

file.close()
