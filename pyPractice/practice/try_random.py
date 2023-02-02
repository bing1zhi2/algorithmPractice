# coding:utf-8

import random

count1 = 0
count2 = 0
times = 10000

for i in range(times):
    aaa = random.choice(range(10))
    print(aaa)
    if aaa >= 3:
        count1 += 1
    else:
        count2 += 1

print(count1 / times)
print(count2 / times)
# random.