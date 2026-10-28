# def add(a: int, b: int) -> int:
#     # 标明a和b的数值类型,   以及结果的数值类型
#     return a + b
#
#
# def greet(name: str) -> str:
#     return f'你好，{name}'
#
#
# names: list[str] = ['小明', '小红']
# # names = ['小明', '小红']
# info: dict[str, int] = {'age': 20}
# # info: = {'age': 20}
#
# print(add(1, 2), greet('小明'), names, info)
'''
练习
'''


# 下面的函数没有注解，补全它
def multiply(a: int, b: int) -> int:
    return a * b


def is_adult(age: int) -> bool:
    return age >= 18


'''
# 用类型注解声明下面三个变量：
# ① 一个存学生名字的列表
# ② 一个"姓名 → 成绩"的字典
# ③ 一个坐标点 (x, y)，两个都是整数
'''
names: list[str] = []
info: dict[str, int] = {}
point: tuple[int, int] = (0, 0)

'''
# 写一个函数 split_name：
# 参数是字符串（如 "张 三"），返回拆开后的列表（如 ['张', '三']）
# 参数和返回值都要加注解
'''

# def split_name(name: str) -> list[str]:
#     return name.split()
#
#
# print(split_name('张三'))
'''
# 写一个函数 print_hello：
# 接收一个名字，打印"你好，xx"，不返回任何东西
# 它的返回值该注解成什么？
'''


def print_hello(name: str) -> None:
    print(f'你好,{name}')


print(print_hello('wcz'))

'改错'


# 下面代码有类型问题，找出哪几行不对，并说明为什么
def get_age(name: str) -> int:
    return 18


ages: list[int] = [20, 25, 30]

name: str = '123'
