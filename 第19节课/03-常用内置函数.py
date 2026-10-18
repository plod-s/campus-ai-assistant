'''
int
float
string
list
tuple
set
dict
'''

num1 = 10  # 大于零的数据我们称之为正数
num2 = -10  # 小于零的数据我们称之为负数
'''
abs:绝对值函数
'''
# print(abs(num2))

'''
min():求最小值
max():求最大值
只能在一个序列里面求值---多个值之间进行比较
sum():求和
'''
# lst = [1, 2, 3, 4, 5]
# t = (1, 2, 3, 4, 5)
# print(max(lst))
# print(min(t))

'''
列表---排序---sort()---reverse
1.上面这两个方法---只能列表使用
2.调用这两个方法直接修改的是原列表
sorted reversed()   
1.不局限于列表，元组依然可以使用
2.这两个方法不会更改原列表可以直接打印
也就是说这两个函数里面有return的返回值可以用的时候打印出来


总结:sort和reverse，没有返回值return,就不能直接打印，想要做修改只能作为一个程序员去修改
而sorted和reversed，有返回值returned,就可以直接打印,想要做修改只需正常的作为用户去修改未知参数即可

启发:有return返回值的函数可以直接打印，调用函数时作为用户调用函数名来修改
没有return返回值的函数不能够直接打印,
'''
# lst = [2, 5, 23, 435, 7, 4, 2, 67, 89, 0]
# lst.sort()
# print(lst)
# lst.reverse()
# print(lst)

# 三个独立列表
names = ['张三', '李四', '王五']
posts = ['柜员', '经理', '会计']
salaries = [1000, 2000, 3000]

'''
有一个工具函数zip，将里面的数据进行一一对应
返回的是一个压缩包---解压缩---将他的数据类型变一下就好了
以最短的列表为准,多出来的元素会被忽略
'''
# print(names[0],posts[0],salaries[0])
print(list(zip(names, posts, salaries)))
