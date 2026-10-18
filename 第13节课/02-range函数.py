'''
for  in :关键字
变量:接受你每一次死循环的值
'''
# 整数/浮点数/bool 不能直接进行for循环
# for item in str(124.0):
#     print(item)
'''
范围/区间
range(起始值,结束值,步长):整数序列(一系列多个数字,整数)
其实只默认是从0开始,结束值必须要写,补偿默认从1开始
'''
# 0 1 2 3 4
# for n in range(5):
#     print(n)

# 1-10  1-11
# for i in range (1,11):
#     print(i)

'''
生成1- 100的偶数
'''
# for i in range(2, 101, 2):
#     print(i)

# for i in range(100, 0, -2):
#     print(i)

'''
数字包含3或者是3的倍数,不说数字,说'过'
条件包含判断---if
包含3---in 运算符  变成str---字符串
如果是3的倍数,取余之后,结果会是0
1--100
'''
for n in range(1, 101):
    if n % 3 == 0 or '3' in str(n):
        print('*')
    else:
        print(n)
