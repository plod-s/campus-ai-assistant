info = ['CEO浅', '总经理兵', '财务心', '运营从', '业务米']

# 运营从---运营总监 replace?
# replace --- 字符串专用
# list---
'''
列表这个数据类型是没有replace方法
AttributeError: 'list' object has no attribute 'replace'
属性方法错误    :   列表   对象     没有  属性方法     替换
列表[索引] = 新值
'''
info[3] = "运营总监从"
# CEO---不开心
info[0] = 'CEO不开心'

# '财务新','运营从','业务米' --- 财务海 运营舍得 业务追风
info[2:] = ["财务海", "运营舍得", "业务追风"]
print(info)
