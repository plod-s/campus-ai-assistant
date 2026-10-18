'''
.:replace(旧字符,新字符): 替换
'''
s1 = "这是一个垃圾食品"
# 垃圾---**---replace
# new_s1 = s1.replace("垃圾", "**")
# print()

s2 = "1234546678"
# 电话号码中间四位屏蔽 旧字符  新字符
'''
1236---中间四位(位置不会发生变化)
先通过切片的方式---将中间四位提取出来
'''
# print(s2.replace(s2[3:7], '****'))

# 用户在注册---不小心前后加了个空格
'''
.strip(字符):自动去除前后的符号,默认去除空格
TypeError: strip expected at most 1 argument, got 2
类型错误      strip            最多     参数 
'''
user_name = " qianan"  # 自动把数据做清理
user_name1 = "##qianan$$"  # 自动把数据做清理
# print(user_name.strip())
print(user_name1.strip('#$'))  # 单个去除你指定的字符

name1 = '####qianan$$$$'
print(name1.lstrip('#'))

'''
浅安,18,长沙,12423543265
'''
# s3 = '浅安,18,长沙,12423543265'
s3 = 'K465|7:30|A56|9:30'
# print(s3.split(','))
# print(s3.split("|"))  # 对于字符个数不确定,

'''
count---计数
find---查找
index---查找
'''
# 词云图
s4 = '这个商品很好,好评,质量不错,给个大大的好评!'
print(s4.count("好评"))  # 查找好评出现的次数

# 想要查看这一串字符串里面是否包含好评
print(s4.find('好评'))  # 返回查找的索引位置
print(s4.find('差评'))  # 当没有查找到这个值的时候,打印输出-1

# print(s4.index("差评"))  # 当没有查找到护照的这个值的时候，直接报错
'''
ai---帮你自动整理文件---把你的文件进行归类
靠的是文件名的后缀进行分类
文本文档---.txt
word----.docx
图片----png,jpg,jpeg
'''
filename = "百度.png"
print(filename.endswith('.png'))  # 判断你这个字符串的后缀名是不是png
'''
注册个人---验证码  a3B5---A3B5(大部分，不会区分大小写)
用户的体验感---
内部---统一转成大写  小写
upper():统一转换成大写
lower():统一转换成小写
'''
# print("a3B4".lower() == "A3B5".lower()) # 考虑用户体验感以及正确性

print('123214a'.isdigit())
