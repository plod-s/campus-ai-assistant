'''
lst---可变
集合---可变
'''
week1 = {'海同学', '潘同学', '时光同学', '蒋同学'}
# print(week1[0])
# 添加数据---add(添加的值)
# week1.add('健健同学')
# print(week1)

# 删除---remove
# week1.remove('海同学')
# print(week1)
# week1.pop()  # 随机删除值
# print(week1)

# 改  要加{}!!因为本质添加,应该添加
week1.update({'海同学', '星空同学'})
print(week1)
# 清空集合里面的所有元素
# week1.clear()
# print(week1)

