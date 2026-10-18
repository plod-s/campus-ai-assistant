print('*' * 5 + '欢迎来到SongBai超级市场' + '*' * 5)
print('-' * 12 + '购物小票' + '-' * 12)
print('名称', '价格', '数量', '折扣')

shui_guo = input('请输入你买的物品:')
jia_ge = float(input('请输入物品的价格:'))
shu_liang = float(input('请输入购买的数量:'))
zhe_kou = 0.85

print(f"{shui_guo}   {jia_ge}   {shu_liang}   {zhe_kou}")
print('-' * 12 + '商品结算' + '_' * 12)
ying_shou = jia_ge * shu_liang * zhe_kou
shi_shou = float(input('请输入实收:'))
zhao_ling = shi_shou - shu_liang

print('应收:', ying_shou)
print('实收:', shi_shou)
print('找零:', zhao_ling)
