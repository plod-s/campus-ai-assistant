dic = {"name": "小美", "id": "A001", "dept": "开发部", "salary": 15000}

# 查询薪资:必须通过键查询
# print(dic["salary"])
# print(dic.get["salary"])

# 区别:查询字典当中不存在的键
# print(dic["薪水"])
print(dic.get("薪水", ))
