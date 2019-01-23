class H20:
    def __init__(self, name, temperature):
        self.name = name
        self.temperature = temperature

    def turn_ice(self):
        if self.temperature <= 0:
            print('[%s]温度太低结冰了' %self.name)
        elif self.temperature > 0 and self.temperature < 100:
            print('[%s]液化成水' %self.name)
        else:
            print('[%s]温度太高气化成水蒸气了' %self.name)


class Water(H20):
    pass

class Ice(H20):
    pass

class Steam(H20):
    pass

w1 = Water('水', 25)
w2 = Ice('冰', -10)
w3 = Steam('水蒸气', 100)

w1.turn_ice()
w2.turn_ice()
w3.turn_ice()