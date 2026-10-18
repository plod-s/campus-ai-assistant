# 1. 变量命名只能有字母\数字\下划线组成，并且数字不能开头
name1 = '浅安'
name_1 = "浅安"
_name = "浅安"
name = "浅安"
# 2. 变量名尽量做到见名之意
# 3. 变量名可以用中文命名---不建议(编码问题)
金钱 = 160
# print(金钱)
# 4.python严格区分大小写
a = 1
print(A)  # NameError: name 'A' is not defined
'''
NameError: 姓名错误--变量名错误
name 'A' is not defined
name A 没有被定义
'''
print(a)
# 5. 变量名不能与python关键字重名---python里面征用了一些单词
# import keyword
# print(keyword.kwlist)
False1 = 1


