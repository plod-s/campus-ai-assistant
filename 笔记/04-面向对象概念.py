'''
老板----定制员工(多个)
设定了一个员工类:
    1. 员工姓名, 员工性别, 员工年龄---变量存储---属性
    2. 前台, 业务, 内勤, 财务, 设计等等---函数---方法
'''


# 定义一个类: class
class Person:
    def qiantian(self):
        print('拥有前台工作内容的能力')

    def yewu(self):
        print('拥有业务能力')

    def caiwu(self):
        print('拥有财务管理的能力')


p1 = Person()  # 创建出员工1号
p1.qiantian()  # 让p1这个员工去干前台的活
p1.yewu()

p2 = Person()
p2.caiwu()