class LazyProperty:
    def __init__(self, func):
        # print('*' * 12)
        self.func = func

    def __get__(self, instance, owner):
        if instance is None:
            return self
        # print(instance)
        # print(owner)
        print('-' * 36)
        res = self.func(instance)
        setattr(instance, self.func.__name__, res)
        return res

class Room:
    def __init__(self, name, width, length):
        self.name = name
        self.width = width
        self.length = length

    @LazyProperty
    def area(self):
        return self.width * self.length


room = Room('ksm', 4, 6)
print(room.__dict__)
print(room.area)
print(room.__dict__)
print(room.area)
print(room.area)

# print(Room.__dict__)
