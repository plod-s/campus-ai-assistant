'''
and:两个条件同时满足才会返回True
or:两个条件满足其中一个才会返回True
not:口是心非,对的返回False,错的返回True
'''
# True  and    True---True
print(3 > 2 and 2 > 1)
# True and False----False
print(3 < 2 and 2 < 1)
# True or False
print(3 < 2 or 2 < 1)

print(not (1 > 2))
