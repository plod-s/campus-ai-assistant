'''
老板---定制员工(多个)

1.员工性别,员工年龄,员工身高---变量存储---属性
2.前台,业务,内勤,财务,设计等等--函数--方法
'''


# 定义一个类:class
class Person:
    def qian_tai(self):
        print('拥有前台工作能力')

    def ye_wu(self):
        print('拥有业务的能力')

    def cai_wu(self):
        print('拥有财务管理的能力')


p1 = Person()  # 创建出员工一号
p1.ye_wu()
p1.cai_wu()

p2 = Person()
p2.ye_wu()
