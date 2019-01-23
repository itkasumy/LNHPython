import time

class Open:
    def __init__(self, filename, mode='r', encoding='utf8'):
        # self.filename = filename
        self.mode = mode
        self.encoding = encoding
        self.file = open(filename, mode, encoding=encoding)

    # def read(self):
    #     pass
    #
    def write(self, line):
        t = time.strftime('%Y-%m-%d %X')
        self.file.write('%s %s' %(t, line))

    def __getattr__(self, item):
        # print('no attr called: ', item)
        return getattr(self.file, item)


fi = Open('test.txt', 'w+')
print(fi.read)
fi.write('666666\n')
fi.seek(0)
print(fi.read())
