# class Hand:
#     pass
#
# class Foot:
#     pass
#
# class Trunk:
#     pass
#
# class Head:
#     pass
#
# class Person:
#     def __init__(self, id_num, name):
#         self.id_num = id_num
#         self.name = name
#         self.hand = Hand()
#         self.foot = Foot()
#         self.trunk = Trunk()
#         self.head = Head()


# ksm = Person('420545', 'ksm')
# print(ksm.__dict__)



# class School:
#     def __init__(self, name, addr):
#         self.name = name
#         self.addr = addr
#
# class Course:
#     def __init__(self, name, price, period, school):
#         self.name = name
#         self.price = price
#         self.period = period
#         self.school = school
#
#     def teach(self):
#         print('ksm in teaching...')
#
# sch1 = School('cz', 'shenzhen')
# sch2 = School('cz', 'shanghai')
# sch3 = School('cz', 'wuhan')
#
# cur1 = Course('Python', 18980, 4, sch1)
# cur2 = Course('FE', 19990, 6, sch2)
# cur3 = Course('Golang', 19980, 6, School('km', 'dongguan'))
#
# print(cur1.__dict__)
# print(cur1.school.addr)
