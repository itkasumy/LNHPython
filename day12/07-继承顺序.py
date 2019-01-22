class A:
    pass
    # def test(self):
    #     print('A')

class B(A):
    # pass
    def test(self):
        print('B')

class C(A):
    pass
    # def test(self):
    #     print('C')

class D(B):
    pass
    # def test(self):
    #     print('D')

class E(C):
    # pass
    def test(self):
        print('E')

class F(D, E):
    pass
    # def test(self):
        # print('F')


f = F()
f.test()
print(F.__mro__)