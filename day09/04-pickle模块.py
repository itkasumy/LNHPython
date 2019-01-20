import pickle

dic = {'name': 'ksm', 'age': '24'}

print(type(dic))

j = pickle.dumps(dic)
print(type(j))

# fi = open('序列化对象_pickle', 'wb')
# fi.write(j) # pickle.dump(dic, fi)
# fi.close()

fi_r = open('序列化对象_pickle', 'rb')
data = pickle.loads(fi_r.read())
print(type(data), data)
fi_r.close()
