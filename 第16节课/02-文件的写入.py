'''
一定先打开文件
重新打开文件写入内容---会将文件里面的内容线清空,然后再写入
'''
# 将内容写到一个不存在的文件里面---不会报错---自动给你新建
f = open('bb.txt', 'w', encoding='utf-8')
f.write('你好\n')  # write:写
f.write('我喜欢Python')  # write:写
