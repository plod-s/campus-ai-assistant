class Person:
    # 对于所有对象共享的一个值----可以定义为类属性
    country = '中国'  # 所有对象可以共享

    # 自动赋值的工具-----初始化方法 __init__   (shift+-)
    def __init__(self, xingming, nianling, gangweixinxi, xingbie, qian):
        self.name = xingming  # lzy======p1
        self.age = nianling
        self.gangwei = gangweixinxi
        self.gender = xingbie
        self.__money = qian  # 定义为私有属性, 在python当中,没有真正的私有化---君子论迹不论心

    def get_money(self):
            return self.__money

    def set_money(self, value):
        if value < 0:  # ③ 规矩
            raise ValueError('资产不能是负数')
        self.__money = value  # ② 写

        # ===== 新增到这里结束 =====

    # 参数
    def qiantian(self):  # 当前那个对象去调用这个方法, self就是当前调用的对象
        # p1这个对象去干这个干活  p1
        # p2这个对去干这个活  p2
        print(f'{self.name}拥有前台工作内容的能力, 来自{Person.country}, 他的资产是{self.__money}')

    def yewu(self):
        print('拥有业务能力')

    def caiwu(self):
        print('拥有财务管理的能力')


p1 = Person('小王', 12, 'qiantai', 'nan', 2000)
print(p1.set_money(100))
print(p1.get_money())
print(p1.set_money(-100))
