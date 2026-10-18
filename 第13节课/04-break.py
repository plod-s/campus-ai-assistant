# 有5次抢票机会,第3次抢到手
for i in range(1, 6):
    print(f'第{i}次尝试抢票')
    if i == 3:
        print('抢到票了!')
        break

