class Room:
    def __init__(self, name, owner, width, length, height):
        self.name = name
        self.owner = owner
        self.width = width
        self.length = length
        self.height = height

    @property
    def cal_area(self):
        return '%s 住的 %s 的面积是: %s' % (self.owner, self.name, self.width * self.length)


r1 = Room('rujia', 'ksm', 14, 4.5, 3)
print(r1.cal_area)
