'''
字符串---字符串是不可变的数据类型

replace---替换---新的字符---不会修改原来的字符

'''


# def re(s1):
#     # 字符串前后颠倒
#     # print(s1[::-1])
#     return s1[::-1]
#
#
# data = 'hello'
# # print(data.replace('h', 'H'))
# print(re(data))  # 函数内部是没有将结果返回,没有返回值
#
# print(re('python'))


# return 可以提前结束函数
# 一个函数里面可以拥有多个return吗
# 返回多个参数?
def func1():
    print(111)
    print(2222)
    print(3333)
    return 1,2


num = func1()
print(num)
