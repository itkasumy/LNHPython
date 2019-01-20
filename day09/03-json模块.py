import json

dic = {'name': 'ksm'}

# fi = open('test.json', 'w')
# # data = json.dumps(dic)
# # print(type(data), data)
# # fi.write(data)
# json.dump(dic, fi)
# fi.close()

# fi_read = open('test.json', 'r')
# # data = json.loads(fi_read.read())
# data = json.load(fi_read)
# fi_read.close()
# # print(type(data), data)

# num = 6
# string = 'hello'
# arr = [1, 2, 3, 4, 5, 6]
# print(type(json.dumps(num)), json.dumps(num))
# print(type(json.dumps(string)), json.dumps(string))
# print(type(json.dumps(arr)), json.dumps(arr))

import json

with open('json_text', 'r') as f:
    data = f.read()
    res = json.loads(data)
    print(res['name'])
