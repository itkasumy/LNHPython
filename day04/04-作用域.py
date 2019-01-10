def foo():
    name = 'ksm'
    def bar():
        name = 'ly'
        def fun():
            print(name)
        return fun
    return bar

bar = foo()
fun = bar()
fun()

foo()()()
