'''
int:整型
float:浮点数
bool:布尔
str:字符串
TypeError: can only concatenate str (not "int") to str
类型错误:    能   仅
字符串类型数据不能跟int类型做连接
'''

# s1 = '123'
# print(int(s1) + 2)  # 我想要做相加计算
# print(float(s1) + 2)  # 想要把字符串变成浮点数
# print(type(s1))

# 字符串类型的小数-----只能转化成浮点数
s1 = '520.0'
s2 = 10
print(float(s1)+s2)

s1 = 3434
s2 = str(s1)
print(type(s2))  # 数值类型转为字符串---临时转换 str

num = 4.6
print(int(num))  # 浮点数---取整  4
'''
int:整型
float:浮点数
str:字符串
1.如果你想转换成对应的数据类型   类型名称(转换的值)
2.字符串类型的浮点数---float 不能转换成int
'''
s1 = '520.0'
print(int(float(s1)))

