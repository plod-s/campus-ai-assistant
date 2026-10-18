lst = ['CEO不开心', '总经理兵', '财务海', '运营舍得', '业务追风']
'''
append(数据):在列表的末尾添加一组新的数据
insert(索引,数据):在指定位置添加数据
extend(多组数据):两个列表里面的数据合并到一个列表里面
'''
# 规范化---人事HR
lst.append("人事丹")
print(lst)
# 秘书---在CEO旁边
lst.insert(1, '秘书金')
# ["技术总监乖","技术人员潘","技术人员咕噜"]
info = ["技术总监乖", "技术人员潘", "技术人员咕噜"]
lst.extend(info)
lst.append(info)
print(lst)
