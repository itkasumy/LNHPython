# import configparser
#
# config = configparser.ConfigParser()
# config['DEFAULT'] = {
#     'ServerAliveInterval': '45',
#     'Compression': 'yes',
#     'CompressionLevel': '9'
# }
#
# config['bitbucket.org'] = {}
# config['bitbucket.org']['User'] = 'hg'
# config['topsecret.server.com'] = {}
# topsecret = config['topsecret.server.com']
# topsecret['Host Port'] = '50022'
# topsecret['ForwardX11'] = 'no'
# config['DEFAULT']['Forward11'] = 'yes'
#
# with open('example.ini', 'w') as configfile:
#     config.write(configfile)



# 增删改查
import configparser
config = configparser.ConfigParser()
config.read('example.ini')

# 查
print(config.sections())
print('bytebong.com' in config)
print(config['bitbucket.org']['User'])
print(config['DEFAULT']['Compression'])
print('-' * 36)

for key in config['bitbucket.org']:
    print(key)

print(config.options('bitbucket.org'))
print(config.items('bitbucket.org'))
print(config.get('bitbucket.org', 'compression'))

# 增
config.add_section('ksm')
config.set('ksm', 'skl', '666666')

# 改


# 删
config.remove_section('ksm')
config.remove_option('bitbucket.org', 'user')

config.write(open('i.cfg', 'w'))