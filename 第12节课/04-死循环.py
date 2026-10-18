# 什么条件下为死循环---条件一直成立  bool---True
'''
死循环---无限循环---避开无限循环
需求:
循环次数不确定---无限循环+break

向领导请假---yes,同意  不同意 继续问领导
'''
while True:
    asw = input('领导我想请假，请求批准')
    if asw == 'yes':
        print('谢谢领导批准')
        break
else:
    print('领导我想请假，请求批准')
