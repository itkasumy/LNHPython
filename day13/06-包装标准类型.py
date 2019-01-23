class List(list):
    def showMiddle(self):
        return self[int(len(self) / 2)]

    def append(self, item):
        if type(item) is str:
            super().append(item)
        else:
            print('should be str type only')

ls = List('helloworld')

print(ls, type(ls))
print(list('helloworld'), type(list('helloworld')))

print(ls.showMiddle())
ls.append('www')
print(ls)
ls.append(520)