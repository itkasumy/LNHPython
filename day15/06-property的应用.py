class Goods:
    def __init__(self):
        self.original_price = 100
        self.discount = .8

    @property
    def price(self):
        return self.original_price * self.discount

    @price.setter
    def price(self, val):
        self.original_price = val

    @price.deleter
    def price(self):
        del self.original_price


obj = Goods()
print(obj.price)
obj.price = 200
print(obj.price)
del obj.price
# print(obj.price)
