user_list = [
    {'name': 'ksm', 'password': '123456'},
    {'name': 'cjx', 'password': '123456'},
    {'name': 'wlm', 'password': '123456'},
    {'name': 'ly', 'password': '123456'}

]
curr_dict = {'username': None, 'login': False}

def auth_func(func):
    def wrapper(*args, **kwargs):
        if curr_dict['username'] and curr_dict['login']:
            return func(*args, **kwargs)

        username = input('请输入用户名:').strip()
        password = input('请输入密码:').strip()

        for user_dict in user_list:
            if username == user_dict['name'] and password == user_dict['password']:
                curr_dict['username'] = username
                curr_dict['login'] = True
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