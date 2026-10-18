'''
程序正常结束运行,自动关闭
程序运行过程中,中途报错
'''
# f = open('aaa.txt', 'r', encoding='utf-8')
# # 读
# print(f.read())  # 读取你这个文件里面所有的内容
# # 让光标从头开始
# f.seek(0)
# print(f.read())  # 读取你这个文件里面所有的内容
# f.close()

# 上下文管理器---操作文件关闭之后,会自动关闭文件
with open('aaa.txt', 'r', encoding='utf-8') as f:  # 将这个文件对象赋值给了f这个变量
    # 缩进里面的代码就是你对文件进行的操作
    print(f.read())



'''
文件的模式:open('文件路径','文件模式','编码')
     读:r
     写:w
     追加:a
     混合模式:r+ w+ a+
     二进制:rb  wb  ab
     上下文管理器with open(路径,文件模式,utf-8) as f
'''