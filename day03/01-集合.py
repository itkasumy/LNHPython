st1 = set('hello')
print(st1)

st2 = set(['ksm', 'cih'])
print(st2)

st3 = {1, 2, 3, 4, 5, 6}
st3.add('a')
st3.add('3')
st3.add(3)
print(st3)

# st3.clear()
# print(st3)

st4 = st3.copy()
print(st4)

st3.pop()
print(st3)

st3.remove(3)
print(st3)

st3.discard('abcdef')
print(st3)
