'''
第 1 题 · time 模块

用 time.time() 测出"1 到 100 万求和"的耗时，打印成：耗时 0.08 秒（保留 2 位小数）

'''
# import time
#
# start = time.time()
# sum_0 = 0
# for i in range(1, 1000000):
#     sum_0 = sum_0 + i
# end = time.time()
# time3 = end - start
# print(f'总共耗时:{time3:.2f}秒')
'''
第 2 题 · 异常处理

写一个 AA 分账程序：输入总金额和人数，
用 try/except 处理错误（输入非数字、人数为 0），出错时给友好提示而不是崩溃。

'''
try:
    total = float(input('输入总金额:'))
    sum_people = int(input('输入总人数:'))
    average = total / sum_people
    print(f'每人需要付{average:.2f}元')
except Exception as e:
    print(f'输入的为非数字,人数为0,请重新输入,原因:{e}')
'''
从零复现 04 那个 Person 类：3 个方法 + 创建 2 个实例 + 各调用一个方法
'''


# class Person:
#     def yun_ying(self):
#         print('我能执行运营的工作')
#
#     def cai_wu(self):
#         print('我能执行财务的工作')
#
#     def qian_tai(self):
#         print('我能执行前台对的工作')
#
#
# p1 = Person()
# p1.yun_ying()
# p1.cai_wu()
#
# p2 = Person()
# p2.qian_tai()
class Bank:
    bank_name = '商洛银行'                       # 类属性：所有对象共享

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance                 # ① 私有化

    def get_balance(self):                       # ② 只读通道
        return self.__balance

    def set_balance(self, value):                # ② 可写通道
        if value < 0:                            # ③ 规则
            raise ValueError('余额不能为负')
        self.__balance = value

    def show(self):
        print(f'{self.name}的余额是{self.__balance}')


b = Bank('小明', 100)
print(b.get_balance())        # 100
b.set_balance(500)
print(b.get_balance())        # 500

try:
    b.set_balance(-50)
except ValueError as e:
    print(f'被拦住了：{e}')     # 被拦住了：余额不能为负
