import hashlib

m = hashlib.md5('ksm'.encode('utf8')) # 加盐

# m.update('hello'.encode('utf8'))
# print(m.hexdigest())
#
# m.update('ksm'.encode('utf8'))
# print(m.hexdigest())
# fdb1b851573a575f7b0f287f314b6ab6

m.update('helloksm'.encode('utf8'))
print(m.hexdigest())
# fdb1b851573a575f7b0f287f314b6ab6
