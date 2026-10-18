# num1 = float(input('请输入一个数字:'))
# num2 = float(input('请再输入一个数字:'))
# print('和', num1 + num2)
# print('差', num1 - num2)
# print('积', num1 * num2)
# print(f'商{num1 / num2:.3f}')


# # 苹果价钱
# apple = 8
# apple_num = 3
# # 香蕉价钱
# banana = 5.5
# banana_num = 2
# # 总价钱
# price = apple * apple_num + banana * banana_num
# print(f'应付总金额为:{price:.2f}')
# # 用户输入以及找零
# total_price = float(input('请用户输入金额:'))
# change = total_price - price
# print(f'找零:{change}')
#
# s1 = input('请用户输入手机号:')
# print(s1[0:3] + '****' + s1[7:])

# grade = int(input('请输入你的成绩:'))
# if 0 <= grade <= 100:
#     if grade >= 90:
#         print('优秀很棒很nice!')
#     elif 80 <= grade < 90:
#         print('良好')
#     elif 60 <= grade < 79:
#         print('及格')
#     else:
#         print('不及格')
#     if grade >= 90 or grade < 60:
#         print('该成绩属于优秀或者不及格的极端行列')
# else:
#     print('请输入正确的成绩!')
class f:

    def f1(self):
        print(self.__balance)


def f2(self):
    return self.__balanc


b = f()
print(b.f1())  # 屏幕上先出现 100，然后出现 None
print(b.f2())  # 屏幕上出现 100
