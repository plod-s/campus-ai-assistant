'''
keys():获取所有的键
values():获取所有的值
items():获取所有的键值
'''

dic = {"name": "小美", "id": "A001", "dept": "开发部", "salary": 15000}
# print(dic.keys())
# print(dic.values())
# print(dic.items())
# for i in dic:
#     print(i, dic[i])  # dic['键']----值
# 循环字典的时候,只获取字典的值
# for v in dic.values():
#     print(v)

# 想同时获取字典的键和值
for k, v in dic.items():
    print(k, v)
