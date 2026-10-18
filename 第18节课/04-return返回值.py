'''
取钱
---柜员---操作---拿到钱---给到你
'''


# def qu_qian(money):
#     print('===== 中国建设银行 ATM =====')
#     print('业务:快速取款')
#     print(f'金额:{money}元')  # 函数里面的代码是多变的--参数
#     print(f'币种:人民币')
#     print('请取走你的现金')
#     print('---------------------------')
#     return money  # 内部人员将参数值递给你
#
#
# # 身上有100
# money1 = 100
# yue = qu_qian(100)  # 去银行取钱100
# # 身上的余额---200块钱
# print(money1 + yue)


def qu_qian(money):
    print('===== 中国建设银行 ATM =====')
    print(f'账号:zhanghao')
    print('业务:快速取款')
    print(f'金额:{money}元')  # 函数里面的代码是多变的--参数
    print('币种:人民币')
    print('请取走你的现金')
    print('---------------------------')
    return money  # 将函数内部的值给你递出来---在哪里使用这个工具---返回到哪一个位置


zs = qu_qian(100)  # ---心动---1000
qu_qian(10000)
print(zs - 200 - 500)
