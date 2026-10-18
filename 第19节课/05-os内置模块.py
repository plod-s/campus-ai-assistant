import os

# print(os.listdir())
# print(os.listdir('E:\AI大模型\第二阶段python\pythonProject\第18节课'))

'''
getcwd:查看当前工作的目录是哪一个

'''
# print(os.getcwd())
os.chdir('C:/Users/dell/Desktop')
# 创建一个文件夹
'''
当文件存在的时候,我就不创建文件夹,文件夹不存在,我就创建
'''
# if print(os.path.exists('aaa')):
#     print('文件已经存在了')
# else:
#     os.mkdir('aaa')  # 如果文件存在就报错
# aaa 更改 AAA
os.rename('aaa', 'AAA')
# remove---删除具体的文件
# os.remove('AAA/bbb.txt')

# rmdir---删除对应的文件夹---默认删除的是空文件夹
os.rmdir('AAA')
