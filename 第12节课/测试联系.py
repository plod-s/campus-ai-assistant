'''案例一
小明吃 5 个包子，第 2 个是韭菜馅的，他不吃，直接跳过：
'''
# n = 1
# while n <= 5:
#     if n == 2:
#         n = n + 1
#         continue
#     print(f'小明吃的第{n}个包子')
#     n += 1
# print('吃饱了')
'''
🏦 ATM 自动取款机（while True + break + continue 组合拳）
取款机要一直服务，直到用户输入 0 退出；余额不足要重新输入：
'''
# total = 1000
# while True:
#
#     money = int(input(f'请用户输入要取出的金额{total}:'))
#
#     if money > total:
#         print('账户里的余额不够，请重新输入余额')
#     if money < total:
#         total = total - money
#         print('取出成功')
#         continue
#     if money == total:
#         break
'''案例 5：🔐 密码登录（次数限制 + 账号锁定）
连续输错 3 次密码就锁定账号：'''
# zhang_hao = 123456
# count = 3
#
# while count > 0:
#     num1 = int(input('请用户输入账号:'))
#     if num1 == zhang_hao:
#         print('登录成功')
#         break
#     else:
#         print(f'登录失败，还剩{count}次机会')
#         count = count - 1
# if count == 0:
#     print("错误次数太多，已锁定")
# ---------------------------------------------------------------------------------------------------
# lst = ['wcz', '陕西省渭南市', '20', '男', '计算机专业']
# for i in lst:
#     print(i)
# for i in range(1, 11):
#     if i == 5:
#         continue
#     print(i)
#     if i == 8:
#         break
# psw = 1231
# chance = 3
#
#
# while chance > 0:
#     a = int(input('请用户输入密码:'))
#     if psw == a:
#         print('登录成功,欢迎回来!')
#         break
#
#     chance -= 1
#     if chance > 0:
#         print(f'输入错误,还剩{chance}次机会')
#     else:
#         print('机会已用完,已锁定🔒')
import time

n = 5
while n > 0:
    print(f'火箭还有{n}秒发射')
    time.sleep(1)
    n -= 1
    if n == 0:
        print('火箭发射成功')
