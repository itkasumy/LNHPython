user_list = [
    {'name': 'ksm', 'password': '123456'},
    {'name': 'cjx', 'password': '123456'},
    {'name': 'wlm', 'password': '123456'},
    {'name': 'ly', 'password': '123456'}

]
curr_dict = {'username': None, 'login': False}

def auth(auth_type='filedb'):
    def auth_func(func):
        def wrapper(*args, **kwargs):
            print('认证类型是:%s' %auth_type)

            if auth_type == 'filedb':
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
            elif auth_type == 'ldap':
                print('鬼特么会玩')
            else:
                print('鬼特么都不会玩')

        return wrapper
    return auth_func

@auth(auth_type='filedb')

def index():
    print('欢迎来到网站首页')

@auth(auth_type='ldap')
def home(name):
    print('欢迎回家%s' %name)

@auth(auth_type='fidb')
def shopping_car():
    print('购物车里空空如也')

index()
home('ksm')
shopping_car()