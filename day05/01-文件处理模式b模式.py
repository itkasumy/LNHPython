# file = open('', 'rb', encoding='utf8') # b的方式不能指定编码
file = open('hexinlang', 'rb')
data = file.read()
print(data)
print(data.decode('utf8'))
file.close()

# string01 = '''
#     即事笔尖扫尽痴云，
#     歌声唤醒芳春。
#     花担安排酒樽。
#     海棠风信，
#     明朝陌上吹尘。
#     一从鞍马西东，
#     几番衾枕朦胧，
#     薄幸虽来梦中。
#     争如无梦，
#     那时真个相逢。
#     隔窗谁爱听琴？
#     倚帘人是知音，
#     一句话当时至今。
#     今番推甚，
#     酬劳凤枕鸳衾。
# '''
#
# string02 = '''
#     莺莺燕燕春春，
#     花花柳柳真真，
#     事事风风韵韵。
#     娇娇嫩嫩，
#     停停当当人人。
# '''
#
# file = open('tianjingsha', 'wb')
# bs = bytes(string01, encoding='utf8')
# file.write(bs)
# file.close()
#
# file = open('tianjingsha', 'ab')
# file.write(string02.encode('utf8'))
# file.close()
