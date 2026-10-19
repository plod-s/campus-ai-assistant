class Person:
    # 对于所有对象共享的一个值----可以定义为类属性
    country = '中国'   # 所有对象可以共享

    # 自动赋值的工具-----初始化方法 __init__   (shift+-)
    def __init__(self, xingming, nianling, gangweixinxi, xingbie, qian):
        self.name = xingming  # lzy======p1
        self.age = nianling
        self.gangwei = gangweixinxi
        self.gender = xingbie
        self.money = qian

    # 参数
    def qiantian(self):  # 当前那个对象去调用这个方法, self就是当前调用的对象
        # p1这个对象去干这个干活  p1
        # p2这个对去干这个活  p2
        print(f'{self.name}拥有前台工作内容的能力, 来自{Person.country}')

    def yewu(self):
        print('拥有业务能力')

    def caiwu(self):
        print('拥有财务管理的能力')


# 当我们创建对象的时候,就会主动触发执行init方法
p1 = Person('lzy', 20, '全能型', '男', '100万')  # 既然都是要做赋值-----封装成一个方法---专门用于赋值工具
p1.qiantian()  # 工作留痕-----谁干了这个活 每个对象没有他专属个性特征(属性)

p2 = Person('时光', 25, '全能型', '女', '200万')
p2.qiantian()