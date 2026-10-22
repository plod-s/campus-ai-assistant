class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f'我是{self.name}，{self.age}岁')


class Student(Person):
    def __init__(self, name, age, school):
        super().__init__(name, age)      # ← 先注释掉
        self.school = school

    def introduce(self):
        super().introduce()                 # ← 也先注释掉
        print(f'我在{self.school}上学')


s = Student('小明', 20, '商洛学院')
print('柜子里有：', s.__dict__)            # {'school': '商洛学院'}
print(hasattr(s, 'name'), hasattr(s, 'age'), hasattr(s, 'school'))   # False False True
s.introduce()