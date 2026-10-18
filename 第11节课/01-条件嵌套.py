# power = False  # 为True代表开机状态 False 关机状态
# dl = 45  # 电量
#
# # 首先判断无人机是否开机
# if power:
#     print('无人机:设备已开机')
#     # 电量>=60 就起飞
#     if dl >= 60:
#         print('可以🛫️')
#     else:
#         print('电量不足,请先充电')
# else:
#     print('无人机还未开机,请先开机')

'''
判断你晚餐是否吃了
如果你没有吃
    身上如果有100那就去吃火锅
    身上有50块钱,会吃快餐
    身上有20块钱,泡面
回家睡觉
'''
eat = input('请问吃饭了吗?Yes/No:')
if eat.lower == 'No':  # no , NO ,No , nO,lower():转小写  upper:转大写
    print('还没吃....')
    money = float(input('请问身上还剩下多少钱'))
    if money >= 100:
        print('去吃火锅')
    elif 50 <= money < 100:
        print('吃牛肉面')
    elif 20 <= money < 50:
        print('吃泡面')
else:
    print('吃了...回家睡觉')
