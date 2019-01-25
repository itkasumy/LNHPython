def Typed(**kwargs):
    def deco(obj):
        # for key in kwargs:
        #     obj.__dict__[key] = kwargs[key]
        # for key, val in kwargs:
        #     obj.__dict__[key] = val
        for key, val in kwargs.items():
            setattr(obj, key, val)
        return obj
    return deco

@Typed(x=1, y=2, z=3)
class Foo:
    pass

print(Foo.__dict__)
fi = Foo()
