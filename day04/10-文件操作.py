# file = open('hexinlang', encoding='utf-8')
# data = file.read()
# print(data)
# file.close()

# file = open('hexinlang', 'r', encoding='utf-8')
# print(file.readable())
# file.close()
#
# file = open('hexinlang', 'w', encoding='utf-8')
# print(file.readable())
# file.close()

# file = open('hexinlang', encoding='utf-8')
# data = file.readline()
# print(data)
# data = file.readline()
# print(data)
# data = file.readline()
# print(data)
# file.close()

# file = open('hexinlang', encoding='utf-8')
# data = file.readlines()
# print(data)
# file.close()

# file = open('tianjingsha', 'w', encoding='utf-8')
# print(file.readable())
# print(file.writable())
# file.write('即事笔尖扫尽痴云，\n')
# file.write('歌声唤醒芳春。\n')
# file.write('花担安排酒樽。\n')
# file.writelines(['海棠风信，\n', '明朝陌上吹尘。\n', '一从鞍马西东，\n', '几番衾枕朦胧，\n', '薄幸虽来梦中。\n', '争如无梦，\n', '那时真个相逢。\n', '隔窗谁爱听琴？\n', '倚帘人是知音，\n', '一句话当时至今。\n', '今番推甚，\n', '酬劳凤枕鸳衾。\n'])
# file.close()
#
# file = open('tianjingsha', 'a', encoding='utf-8')
# print(file.readable())
# print(file.writable())
# file.write('莺莺燕燕春春，\n')
# file.write('花花柳柳真真，\n')
# file.writelines(['事事风风韵韵。\n', '娇娇嫩嫩，\n', '停停当当人人。\n'])
# file.close()

# ??????????????
# file = open('ksm', 'r+', encoding='utf-8')
# # data = file.read()
# # print(data)
# file.write('hello ')
# file.close()

# src_file = open('tianjingsha', 'r', encoding='utf-8')
# data = src_file.read()
# src_file.close()
#
# dst_file = open('tjs_new', 'w', encoding='utf-8')
# dst_file.write(data)
# dst_file.close()

with open('tjs_new', 'r', encoding='utf-8') as src_file,\
    open('tjs_new_new', 'w', encoding='utf-8') as dst_file:
    data = src_file.read()
    dst_file.write(data)
