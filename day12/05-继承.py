class Father:
    money = 100

    def __init__(self, name):
        self.name = name
        print('father')

    def work(self):
        print('%s is working' %self.name)

class Son(Father):
    money = 1000

# print(Son.money)

gc = Son('ksm')
print(gc.money)
gc.work()
