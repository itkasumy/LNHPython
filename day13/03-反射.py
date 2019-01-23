class BlackMedium:
    feture = 'Ugly'
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr

    def sell_house(self):
        print('【%s】 正在卖房子...' %self.name)

    def rent_house(self):
        print('【%s】 正在出租 %s 的一处房子' %(self.name, self.addr))


zr = BlackMedium('自如', 'baoan')
# zr.sell_house()
# zr.rent_house()

print(hasattr(zr, 'addr'))
print(getattr(zr, 'name'))
print(getattr(zr, 'rent_house'))
rt_zr = getattr(zr, 'rent_house')
rt_zr()

print(getattr(zr, 'rt_house', '没有此属性'))
# print(getattr(zr, 'rt_house'))

setattr(zr, 'pro', 'internet')
print(zr.__dict__)
setattr(zr, 'zone', 'shenzhen')
print(zr.__dict__)

delattr(zr, 'zone')
print(zr.__dict__)

setattr(zr, 'calc', lambda x: x + 1)
print(zr.calc(6))
