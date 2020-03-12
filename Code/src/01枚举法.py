#如果 a+b+c=1000，且 a^2+b^2=c^2（a,b,c 为自然数），如何求出所有a、b、c可能的组合?

import time
i = 0

start_time = time.time()
#
# for a in range(0, 1001):
#     for b in range(0, 1001):
#         for c in range(0, 1001):
#             if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2:
#                 print("第 %d 种可能" % (i + 1))
#                 print("结果是：a, b, c : %d, %d, %d" % (a, b, c))
#                 print("此次耗时： %fs" % (time.time() - start_time))
#                 start_time =  time.time()
#                 i += 1
#                 print("---------------------------------------------")



#改进
for a in range(0, 1001):
    for b in range(0, 1001):
        c = 1000 - a - b
        if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2:
            print("第 %d 种可能" % (i + 1))
            print("结果是：a, b, c : %d, %d, %d" % (a, b, c))
            print("此次耗时： %fs" % (time.time() - start_time))
            start_time =  time.time()
            i += 1
            print("---------------------------------------------")


print("寻找完毕")
end_time = time.time()

print("寻找耗时总时长为： %fs" % (end_time - start_time))



'''
相同程序在不同机器上运算时间不一致
但是执行基本运算数量大体相同

'''