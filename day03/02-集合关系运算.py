python = ['ksm', 'xml', 'xh', 'ly']
fe = ['ksm', 'xml', 'whz', 'gc']

# py_and_fe = []

# for p_name in python:
#     if p_name in fe:
#         py_and_fe.append(p_name)
#
# print(py_and_fe)

py_s = set(python)
fe_s = set(fe)
print(py_s, fe_s)

# 交集
print('-' * 36)
print(py_s.intersection(fe_s))
print(py_s & fe_s)

# 并集
print('-' * 36)
print(py_s.union(fe_s))
print(py_s | fe_s)

# 差集
print('-' * 36)
print(py_s.difference(fe_s))
print(fe_s.difference(py_s))

# 补集
print('-' * 36)
print(py_s.symmetric_difference(fe_s))

# 差集更新
print('-' * 36)
# py_s.difference_update(fe_s)
# print(py_s)

fe_s.difference_update(py_s)
print(fe_s)

# isdisjoint 是否无交集
print('-' * 36)
st1 = {1, 2, 3}
st2 = {4, 5, 6}
st3 = {1, 6, 7}
print(st1.isdisjoint(st2))
print(st1.isdisjoint(st3))
print(st2.isdisjoint(st3))

# issubset 是否是子集
print('-' * 36)
st4 = {1, 2, 3}
st5 = {1, 2, 3, 4, 5, 6}
print(st4.issubset(st5))
print(st5.issubset(st4))

# issuperset 是否是父集
print('-' * 36)
print(st4.issuperset(st5))
print(st5.issuperset(st4))

# update 更新多个值
print('-' * 36)
st4.update(st5)
print(st4)

# 不可变集合的定义
print('-' * 36)
st6 = frozenset('hello')
print(st6)

# 去重列表
print('-' * 36)
ls1 = [1, 3, 2, 6, 3, 1, 4, 7, 3]
print(ls1)
ls1 = list(set(ls1))
print(ls1)