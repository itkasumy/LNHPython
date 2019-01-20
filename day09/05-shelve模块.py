import shelve

fi = shelve.open(r'shelve')

fi['stu_info'] = {'name': 'ksm', 'age': 18}

print(fi.get('stu_info')['name'])

fi.close()
