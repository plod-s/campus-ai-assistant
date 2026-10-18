def ding_qi():
    print(f'已存定期---0.2')


def huo_qi():
    print(f'已存活期---0.1')


def cun_qian(hello):
    # 这里的hello相当于是一个接受的介质，没有真正的含义，也不会做为函数的变量
    hello()


cun_qian(ding_qi)  # 这里调用函数cun_qian之后里面又是ding_qi函数,
# 相当于cun_qian函数中的 hello = ding_qi()也就是
# cun_qian(ding_qi()):----连续调用了两次
