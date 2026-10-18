'''
第一中导入方法:import+模块
缺点:每次运用模块的时候需要写前缀
是把整个工具箱都搬过来
'''
# import demo

# demo.func1()
# demo.func2()


'''
第二种方法:from 模块名 import XXX
多个工具之间要用逗号隔开
xxx就是工具，用哪几个写就行了
'''
# from demo import func1, func2
#
# func2()
# func1()


'''
第三种:import xx as 新名字
适用于当模块名字很长的时候简便
'''

from demo import func2func2func2func2func2 as func2

func2()
