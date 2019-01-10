name = 'ksm'

def change_name1():
    print('My name is', name)

change_name1()
print(name)

def change_name2():
    name = 'xml'
    print('My name is', name)

change_name2()
print(name)

def change_name3():
    global name
    name = 'xml'
    print('My name is', name)

change_name3()
print(name)
 