# # 全局变量作用域---就是在当前的py文件中全局有效
# all_money = 100000
#
#
# def save_money():
#     # 局部变量函数作用域---只能在函数内部使用
#     # 如果需要修改全局变量---需要做一个声明gloabal
#     global all_money  # 在申请修改权限
#     all_money -= 200
#     money = 1000
#     print(money)
#     print(f'在函数内部使用全局变量:money={all_money}')
#
#
# # 执行函数内部代码---必须先调用函数
# save_money()
# print(f'在函数外部使用全局变量:money={all_money}')
# # print(money)  # name 'money' is not defined


def func_baba():
    baba_money = 1000

    # 作用域只属于他上级函数
    def func_son():
        # 当需要用外层函数的变量时---需要用nonlocal调用声明
        nonlocal baba_money
        son_money = baba_money - 100
        print(son_money)
    # 当需要测试时嵌套函数时---在内层调用
    func_son()


func_baba()
