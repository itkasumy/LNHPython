class Vehicle:
    country = 'China'

    def __init__(self, name, speed, load, power):
        self.name = name
        self.speed = speed
        self.load = load
        self.power = power

    def run(self):
        print('start run ...')


class Subway(Vehicle):
    def __init__(self, name, speed, load, power, line):
        # Vehicle.__init__(self, name, speed, load, power)
        super().__init__(name, speed, load, power)
        self.line = line

    def showInfo(self):
        # Vehicle.run(self)
        super().run()
        print(self.line)


line5 = Subway('深圳地铁', '240km/h', 100000, 'electr', 5)
line5.showInfo()