import re

res = re.findall('I\b', 'hello I am LIST')
print(res)

res = re.findall(r'I\b', 'hello I am LIST')
print(res)

res = re.findall('I\\b', 'hello I am LIST')
print(res)

res = re.findall('ks|m', 'ksmakmakcmks')
print(res)

res = re.findall(r'ks|m', 'ksmakmakcmks')
print(res)

# 分组
res = re.findall('(abc)+', 'abcabcabc')
print(res)

print(re.search('(abc)', 'abcabcabc').group())

print(re.search('(?P<name>[a-z]+)\d+', 'ksm24xml22ly21'))
print(re.search('(?P<name>[a-z]+)\d+', 'ksm24xml22ly21').group())
print(re.search('(?P<name>[a-z]+)\d+', 'ksm24xml22ly21').group('name'))
print(re.search('(?P<name>[a-z]+)(?P<age>\d+)', 'ksm24xml22ly21').group('name'))
print(re.search('(?P<name>[a-z]+)(?P<age>\d+)', 'ksm24xml22ly21').group('age'))

print(re.match('\d+', '3ksm24xml22ly21'))
print(re.match('\d+', '3ksm24xml22ly21').group())

print(re.split('[ac]', 'etabcdcdday'))

print(re.sub('\d+', 'KSM', 'ksm24xml22ly21'))
print(re.subn('\d+', 'KSM', 'ksm24xml22ly21'))

com = re.compile('\d+')
print(com.findall('ksm24xml22ly21'))

it = re.finditer('\d+', 'ksm24xml22ly21')
print(it.__next__().group())
print(it.__next__().group())
print(it.__next__().group())

print(re.findall('www\.(baidu|163)\.com', 'fajdslwww.baidu.comlao'))
print(re.findall('www\.(?:baidu|163)\.com', 'fajdslwww.baidu.comlao'))
