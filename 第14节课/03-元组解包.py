'''
盒子---盒子里面能放很多组数据---1个盒子
'''
# t1 = 浅安
# t2 = 18
# too many values to unpack (expected 2)
# 太多了,值跟变量不匹配
t1, t2, *t3 = ('浅安', 18, 160.9, '158213124')
# print(t1, t2, t3)

# a, b = [1, 2]
# print(a,b)

tuple = ('浅安', 18, 160.9, '158213124')
print(t1, t2, t3)
print(tuple)
