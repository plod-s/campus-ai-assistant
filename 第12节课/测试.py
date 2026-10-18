'''
案例一
小明吃 5 个包子，第 2 个是韭菜馅的，他不吃，直接跳过：
n = 1               # 定义初始值为1
while n <= 5:       # 条件  初始值是否小于等于5
    if n == 2:      # 当吃到第二个包子的时候,停下来
        n += 1      # 继续到第三个包子
    continue          # 跳过韭菜馅包子
    print(f"吃掉第 {n} 个包子 🥟")
    n += 1
print("吃饱啦！")     # 4个包子吃完后就吃饱了
吃掉第 1 个包子 🥟
吃掉第 3 个包子 🥟
吃掉第 4 个包子 🥟
吃掉第 5 个包子 🥟
吃饱啦！

案例 2：🎲 猜数字游戏（break 应用 · 课件练习）
确定一个要猜的数字，给用户 3 次机会；猜对立刻退出，机会用完结束：
# 允许猜几次
count = 3     # 初始值为3
# 要猜的数字
computer_num = 8     #电脑随机的数字为8
while count > 0:
    # 次数 -1
    count -= 1        # 用户没猜一次，次数减一
    # 让用户猜数,并转化为整数
    user_num = int(input("请输入一个0~10之间的整数: "))

    if user_num == computer_num:
        # 猜对了则退出循环，结束程序
        print("你走狗屎运了吗, 这都能猜对!")  # 猜对后，给用户的提示
        break                     #   终止循环
运行效果：
请输入一个0~10之间的整数: 6
请输入一个0~10之间的整数: 8
你走狗屎运了吗, 这都能猜对!
案例 3：🏦 ATM 自动取款机（while True + break + continue 组合拳）
取款机要一直服务，直到用户输入 0 退出；余额不足要重新输入：
balance = 1000   # 卡内余额

while True:

    money = int(input("请输入取款金额(输入 0 退出): "))

    if money == 0:
        print("取款结束，再见！")
        break               # 用户主动退出

    if money > balance:
        print("余额不足，请重新输入！")
        continue            # 跳过本次，重新取款

    balance -= money
    print(f"取款成功，剩余余额 {balance} 元")
💡 这是 while True + break + continue 的经典组合，本节三个知识点全部用上！
案例 4：💰 攒钱计划（数值累加）
每天存 500 元，攒够 10000 元为止，看看需要几天：
target = 10000    # 目标金额
total = 0         # 已攒金额
day = 1           # 天数

while total < target:
    total += 500               # 每天存 500
    print(f"第 {day} 天：已攒 {total} 元")
    day += 1

print(f"🎉 达成目标！一共用了 {day - 1} 天")  # 第20天攒够1W后，天数day又加一了,因此需要减一
第 1 天：已攒 500 元
...
第 20 天：已攒 10000 元
🎉 达成目标！一共用了 20 天
案例 5：🔐 密码登录（次数限制 + 账号锁定）
连续输错 3 次密码就锁定账号：
password = "123456"
chance = 3

while chance > 0:
    pwd = input("请输入密码: ")

    if pwd == password:
        print("✅ 登录成功，欢迎回来！")
        break

    chance -= 1
    if chance > 0:
        print(f"❌ 密码错误，还剩 {chance} 次机会")
    else:
        print("🚫 机会用完，账号已锁定，请联系客服！")
案例 6：🚀 火箭发射倒计时（结合 time 模块）
import time

n = 10
while n > 0:
    print(f"🚀 发射倒计时：{n} 秒")
    time.sleep(1)   # 暂停 1 秒
    n -= 1

print("点火！发射！🔥")
'''
import time

n = 10
while n > 0:
    print(f"🚀 发射倒计时：{n} 秒")
    time.sleep(1)   # 暂停 1 秒
    n -= 1

print("点火！发射！🔥")