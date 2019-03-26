# -*- coding:utf-8 -*-

from collections import deque   #双端队列
dequeQueue = deque(['Eric','John','Smith'])
print(dequeQueue)
dequeQueue.append('Tom')    #在右侧插入新元素
dequeQueue.appendleft('Terry')  #在左侧插入新元素
print(dequeQueue)
dequeQueue.rotate(2)    #循环右移2次
print(dequeQueue)

while len(dequeQueue) > 0 :
    print(dequeQueue.popleft())

a =[1,2,3,4]
a.append(5)
print(a)
a.pop()
print(a)