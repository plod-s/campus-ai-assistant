# def su_she(*xingming, chuanghao):
#     print(f'请输入姓名:{xingming}')
#     print(f'请输入床号:{chuanghao}')
#
#
# print(su_she('wcz', 'lzq', chuanghao='3号'))
def demo():
    a = 1

    def func1():
        print(f'打印a:{a}')

    def func2():
        nonlocal a
        a += 10
        print(f'打印a+之后的结果:{a}')

    return func1, func2


a1, a2 = demo()
a1()
a2()
a1()
b1, b2 = demo()      # 再调一次 demo
b1()                 # 猜：？又等于1了