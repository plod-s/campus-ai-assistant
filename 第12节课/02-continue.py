# 当跑到第3圈的时候，想偷懒，不继续跑，从第四圈开始跑
n = 1
while n <= 4:
    if n == 3:
        n += 1
        continue
    print(f'跑了第{n}圈')
    n += 1

'''
5个订单 如果订单是正常,就正常发货
3号订单是取消状态
'''
num = 1
while num <= 5:
    if num == 3:
        print(f'订单{num}已取消,跳过处理')
        num += 1
        continue
    print(f'订单{num},正在发货')
    num += 1
