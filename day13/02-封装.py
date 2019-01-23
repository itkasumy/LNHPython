class Person:
    _from = 'earth'
    def __init__(self, id_num, name):
        self.id_num = id_num
        self.name = name


xml = Person('52013', 'yml')

print(xml._from)
