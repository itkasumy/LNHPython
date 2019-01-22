class Chinese:
    '这是一个中国人的类'
    color = 'yellow'

    def eat(self):
        print('eating')

print(Chinese)
print(dir(Chinese))
print(Chinese.__dict__)

print(Chinese.__dict__['color'])
Chinese.__dict__['eat']('')

print(Chinese.__name__)
print(Chinese.__doc__)
print(Chinese.__base__)
print(Chinese.__bases__)
print(Chinese.__module__)
print(Chinese.__class__)

