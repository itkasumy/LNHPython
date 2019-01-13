def auth_func(func):
    def wrapper(*args, **kwargs):
        username = input('请输入用户名:').strip()
        password = input('请输入密码:').strip()
        if username == 'ksm' and password == '123456':
            return func(*args, **kwargs)
        else:
            print('用户名或密码错误')

    return wrapper

@auth_func

def index():
    print('欢迎来到网站首页')

@auth_func
def home(name):
    print('欢迎回家%s' %name)

@auth_func
def shopping_car():
    print('购物车里空空如也')

index()
home('ksm')
shopping_car()