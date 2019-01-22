class Chinese:
    '这是一个中国人的类'
    color = 'yellow'

    def eat(self):
        print('eating')

    def __init__(self, name, age, gender):
        print('start ...')
        self.name = name
        self.age = age
        self.gender = gender
        print('over ...')

ly = Chinese('ly', 21, 'girl')
print(ly)
print(ly.__dict__)
print(ly.color)
print(ly.name)
print(ly.age)
print(ly.gender)
ly.eat()
