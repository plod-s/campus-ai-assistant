name = "浅安"  # 姓名
age = 18  # 年龄
height = 160  # 身高
weight = 50  # 体重
phone = '1234567890'  # 电话号码
print(name, age, height, weight, phone)
# 要打印一串完整的字符串信息，有包含固定的字符串+变量
# print('我的姓名是:', name, '我的年龄是:', age, height, weight, phone)

'''
挖坑填坑
01---%d---整数 %f---浮点数 %s---字符串
\n:换行符号
'''
# print('我的姓名是:%s\n我的年龄是:%d\n我的身高是:%f\n我的体重是:%f\n我的电话号码是:%s\n' %(name, age, height, weight,phone))
'''
第二代: format
'''
print("我的姓名是{}，我的年龄是{}岁\n我的身高是{}cm\n我的体重是{}kg\n我的电话号码是{}。".format(name, age, height, weight,
                                                                                              phone))
'''
第三代:f""----python3.6以上的版本
'''
# print(f"我的名字是{name},我的年龄是{age},我的身高是{height},")

name = "中原狼"
score = 89.99
# 保留几位小数   存在精度计算---decimal
print(f'姓名是{name},成绩是{score:.2f}')
print(f'姓名是{name},成绩是{score:.3f}')
