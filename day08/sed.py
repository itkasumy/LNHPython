import os

def fetch(data):
    # print('\033[1;43m这是查询功能\033[0m')
    # print('\033[1;43m用户输入的数据是\033[0m %s' %data)

    backend_data = 'backend %s' %data
    with open('haproxy.conf', 'r') as read_f:
        flag = False
        res = []
        for read_line in read_f:
            if read_line.strip() == backend_data:
                flag = True
                continue
            if flag and read_line.startswith('backend'):
                break
            if flag:
                print('\033[1;45m %s \033[0m' %read_line)
                res.append(read_line)

    return res

def add():
    print('这是添加功能')

def change(data):
    print('这是修改功能')
    # print('用户输入的数据是：%s' %data)
    backend = data[0]['backend']
    backend_data = 'backend %s' %backend
    old_server_record = '%sserver %s %s weight %s maxconn %s\n' %(' ' * 8, data[0]['record']['server'], data[0]['record']['server'], data[0]['record']['weight'], data[0]['record']['maxconn'])
    print('用户想要修改的数据是：', old_server_record)
    new_server_record = '%sserver %s %s weight %s maxconn %s\n' %(' ' * 8, data[1]['record']['server'], data[1]['record']['server'], data[1]['record']['weight'], data[1]['record']['maxconn'])

    res = fetch(backend)
    res.insert(0, '%s\n' %backend_data)
    # print('来自change函数:', res)

    if not res or old_server_record not in res:
        return '您要修改的数据不存在'
    else:
        index = res.index(old_server_record)
        res[index] = new_server_record
        print(res)

    with open('haproxy.conf', 'r') as read_f,\
        open('haproxy.conf_new', 'w') as write_f:
        flag = False
        tag = True
        for read_line in read_f:
            if read_line.strip() == backend_data:
                flag = True
                continue
            if flag and read_line.startswith('backend'):
                flag = False
            if flag:
                if tag:
                    for record in res:
                        write_f.write(record)
                    tag = False
            else:
                write_f.write(read_line)

    os.rename('haproxy.conf', 'haproxy.conf.bak')
    os.rename('haproxy.conf_new', 'haproxy.conf')
    # os.remove('haproxy.conf.bak')


def delete():
    print('这是删除功能')

if __name__ == '__main__':
    msg = '''
    1. 查询
    2. 添加
    3. 修改
    4. 删除
    5. 退出
    '''

    msg_dict = {
        '1': fetch,
        '2': add,
        '3': change,
        '4': delete
    }

    while True:
        print(msg)
        choice = input('请输入你的选项:').strip()
        if not choice: continue
        if choice == '5': break

        data = input('请输入你的数据:').strip()
        if choice != 1:
            data = eval(data)

        res = msg_dict[choice](data)
        print('最终的结果是:', res)

        # [{'backend': 'www.oldboy1.org', 'record': {'server': '2.2.2.4', 'weight': 20, 'maxconn': 3000}},{'backend': 'www.oldboy1.org', 'record': {'server': '2.2.2.5', 'weight': 30, 'maxconn': 4000}}]
