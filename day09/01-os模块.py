import os

print(os.getcwd())

# 更改目录
# os.chdir('..')
# print(os.getcwd())

# print(os.curdir)
# print(os.pardir)

# 创建删除目录
# os.makedirs('a/b/c')
# os.removedirs('a/b/c')
# os.mkdir('a')
# os.rmdir('a')
# print(os.listdir('.'))
# os.remove('demo')

# 重命名
# os.rename('a', 'd')


# info
# print(os.stat('.'))

# 输出操作系统特定的路径分隔符
# print(os.sep)

# 当前平台的行终止符
# print(os.linesep)

# 当前平台的路径分隔符
# print(os.pathsep)

# 当前平台的名字
# print(os.name)

# os.system('calc')

# print(os.environ)

# print(os.path.split('d/b/c'))
# print(os.path.dirname('d/b/c'))
# print(os.path.basename('d/b/c'))

# print(os.path.exists('01-os模块.p'))
# print(os.path.isabs('01-os模块.py'))
# print(os.path.isfile('01-os模块.py'))
# print(os.path.isdir('01-os模块.py'))

print(os.path.join(os.path.dirname('C:\\Users\\Administrator\\Desktop\\LNHPython\\day09\\01-os模块.py'), os.path.basename('C:\\Users\\Administrator\\Desktop\\LNHPython\\day09\\01-os模块.py')))

print(os.path.getatime('01-os模块.py'))
print(os.path.getmtime('01-os模块.py'))