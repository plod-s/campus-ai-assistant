'''
装饰器:装饰器就是一个函数(或类),接受一个函数作为参数,并返回另一个函数
在不改变原有函数的基础上去进行添加额外的功能
'''

import time


def shijian(func):
    print(func)
    def ceshi():
        start = time.time()
        func()
        end = time.time()
        cost = end - start
        print(f'程序运行时间:{cost}')
    return ceshi


@shijian  # demo = shijian(demo)
def demo():  # demo = ceshi(ceshi)
    sum = 0
    for i in range(1, 100001):
        sum += i

demo()# 表面是demo实际调用的是ceshi
