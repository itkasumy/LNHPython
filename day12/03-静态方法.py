class Room:
    originate = 'internet'

    def __init__(self, name, owner, width, length, height):
        self.name = name
        self.owner = owner
        self.width = width
        self.length = length
        self.height = height

    @property
    def cal_area(self):
        return '%s 住的 %s 的面积是: %s' % (self.owner, self.name, self.width * self.length)

    @classmethod
    def prtInfo(cls):
        print('all homes info are from %s' %cls.originate)

    @staticmethod
    def haveAShower(a, b):
        print('having a shower ...', a, b)

    def test(x, y):
        print(x, y)


r1 = Room('rujia', 'ksm', 14, 4.5, 3)
r1.haveAShower(1, 2)
Room.haveAShower(1, 2)

Room.test(1, 2)
# r1.test(1, 2)
print(Room.__dict__)
print(r1.__dict__)

r1.test(1)
