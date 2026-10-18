f = open('bb.txt', 'a+', encoding='utf-8')
f.write('hello')
# 文件的光标
f.seek(0)
print(f.read())
