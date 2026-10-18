# a = 'hello'
# for i in a:
#     print(i)
# print('_' * 30)
# for i in range(10):
#     print(i)
# print('_' * 30)
# for i in range(1, 6):
#     print(i)
# print('_' * 30)
# for i in range(2, 11, 2):
#     print(i)
'''
for,in ,range为关键字
i为变量，打印这个i主要是看循环是什么，也就是说这个i是看结果的一种指导,
range后面跟的是容器，主要是看循环在哪里执行且有没有附加条件
range(n)表示取值范围[0,n),取n个值
range(1,6)表示取值为1,2,3,4,5
range(2,11,2)表示取值范围为[2,11),最后面的2表示的是隔一个取一个,如果想隔两个取一个，那就变成3
'''
# for a in range(4):
#     print(a)
# for b in range(1, 10):
#     print(b)
for i in range(21, 2, -1):
    print(i)
# for c in range(10, 51, 10):
#     print(c)
# 3 5 7 9
# 5 8 11 14 17循环次数 = 第二个数字-第一个数字/第三个数数字
# for i in range(1, 6):
#     print("CampusPilot")不清楚这个,我的猜测是
#     根据a = 'hello'
#     for i in a:
#     print(i)的结果,
#     猜测i只是起到了一个对人来说更清晰得看是谁要循环的作用,
#     不用保证和后面print后面的值保持一致
#     最关键的还是要看print的括号里面是啥，才会循环啥
