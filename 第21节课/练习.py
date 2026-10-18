# 写一个 Bank 类：
# 类属性：bank_name = '商洛银行'
# __init__：接收 name, balance 两个参数
# 私有属性：__balance（余额）
# 方法：show() 打印 "xx 在商洛银行的余额是 xx"
# 创建 2 个账户对象，各调用一次 show()
# 在上面的 Bank 类里：
# ① 给 p1 单独设置 p1.bank_name = '广州银行'，打印 p1、p2、Bank 三者的 bank_name
# ② 想想：为什么 p2 没变？（这题答对了说明你懂了类属性）
# 给 Bank 类加两个方法：
#   get_balance()  读余额
#   set_balance(value)  写余额，如果 value < 0 就 raise ValueError("余额不能为负")
# 然后测试：先正常存 100，再试 set_balance(-50) 看会不会被拦住
# class Bank:
#     bank_name = '商洛银行'
#
#     def __init__(self, name, balance):
#         self.name = name
#         self.__balance = balance
#
#     def show(self):
#         print(f'{self.name}在{Bank.bank_name}的余额是{self.__balance}')


# p1 = Bank('s', 12)
# p1.bank_name = '广州银行'
# p2 = Bank('a', 2)
# print(p1.bank_name, p2.bank_name, Bank.bank_name)  # 广州银行 商洛银行 商洛银行
# print(p1.__dict__)          # {'name': 's', '_balance': 12, 'bank_name': '广州银行'}
# print(p2.__dict__)          # {'name': 'a', '_balance': 2}
# print(Bank.__dict__.keys()) # 里面有 bank_name、__init__、show...
'''
每个对象独有的数据 → 放进 __init__，用 self.xxx 存。
所有对象共享、且不会变的常量 → 放类属性。 
永远不要用可变类型（list/dict）当类属性 —— 那是上一条说的经典 bug。'''


# 给 Bank 类加两个方法：
#   get_balance()  读余额
#   set_balance(value)  写余额，如果 value < 0 就 raise ValueError("余额不能为负")
# 然后测试：先正常存 100，再试 set_balance(-50) 看会不会被拦住

class Bank:
    bank_name = '商洛银行'

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def show(self):
        print(f'{self.name}在{Bank.bank_name}的余额是{self.__balance}')

    # ↓↓↓ 新增，写在 show() 下面，缩进和它一样（4 个空格）
    def get_balance(self):
        return self.__balance


b = Bank('小明', 100)

print(b.get_balance())  # 猜：？
