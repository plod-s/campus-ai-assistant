'''
例如AI对用户小习作情绪识别:开心,普通,生气，给出不同回复
'''

# qingxu = input('请输入你的情绪:')
#
# if qingxu == "开心":
#     print('🤖AI:今天心情不错哦😊')
# elif qingxu == "普通":
#     print('🤖AI:那我给你讲个笑话听听😊')
# elif qingxu == '生气':
#     print('🤖AI:可以给我讲讲发生了什么😠')
# else:
#     print('🤖AI:有我在,在心每一天!')


'''
15号发工资
 用户输入他发的薪资,除去固定房租1000,还了花呗500.
 根据他剩下的钱判断他的生活质量
 5000以上:好,优质,小资
 5000-4000:天天烧烤
 4000-3000:管饱,外卖
 3000-2000:自己做饭
 2000-1000:悠着点花
 1000-0:找爸妈借点
'''
money = int(input('请输入薪资:'))
money2 = money - 1000 - 500
if money2 > 5000:
    print('好，优质，小资')
elif money2 <= 5000 and money2 > 4000:  # 4000<money2<=5000
    print('天天烧烤')
elif money2 <= 4000 and money2 > 3000:
    print('管饱,外卖')
elif money2 <= 3000 and money2 > 2000:
    print('自己做饭')
elif money2 <= 2000 and money2 > 1000:
    print('悠着点花')
elif money2 <= 1000 and money2 > 0:
    print('找爸妈借点:')
else:
    print('真喝西北风了')
