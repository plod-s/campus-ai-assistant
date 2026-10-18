class Person:
    country = 'China'

    def __init__(self, name, age, gender, ):
        self.name = name
        self.age = age
        self.gender = gender

    def qian_tai(self):
        print(f'{self.name}拥有前台工作能力,来自{Person.country}')

    def ye_wu(self):
        print(f'{self.name}拥有业务的能力,来自{Person.country}')

    def cai_wu(self):
        print(f'{self.name}拥有财务管理的能力,来自{Person.country}')


p1 = Person('l', 21, 'male')
'''定义一个狗类 Dog：
● 特征（属性）：名字 name、毛色 color
● 行为（方法）：吃 eat、喝 drink、跑 run
'''


class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def eat(self):
        print(f'{self.color}的{self.name}正在吃东西.')

    def drink(self):
        print(f'{self.color}的{self.name}正在喝水.')

    def run(self):
        print(f'{self.color}的{self.name}正在奔跑.')


p11 = Dog('金毛', '黄色')
p11.eat()  # ch
p11.drink()
p11.run()
print(p11.color)
