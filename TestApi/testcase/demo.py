# 题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
# list = [1, 2, 3, 4]
# for i in list:
#     for k in list:
#         for j in list:
#             if (i != k) and (k != j) and (i != j):
#                 print(100*i+10*k+j)

# 企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，
# 可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，
# 可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
I = int(input("请输入利润："))
if I <=100000:
    i = I * 0.1
    print(i)
if 100000 <= I <= 200000:
    i = (I - 100000) * 0.075 + 100000 * 0.1
    print(i)