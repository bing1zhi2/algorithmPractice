# -*- coding:utf-8 -*-

"""
Given an array w of positive integers, where w[i] describes the weight of index i, write a function pickIndex which randomly picks an index in proportion to its weight.

Note:

1 <= w.length <= 10000
1 <= w[i] <= 10^5
pickIndex will be called at most 10000 times.
Example 1:

Input:
["Solution","pickIndex"]
[[[1]],[]]
Output: [null,0]
Example 2:

Input:
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output: [null,0,1,1,1,0]



for the array of {1, 3, 4, 6}
the pickIndex() call will have 1/(1+3+4+6) = 1/14 = ~7% chance of picking index 0; 3/14 = 21% change of picking
index 1; 4/14 = 29% change of picking index 2; and 6/14 = 43% of picking index 3.



"""
import random


class RandomPickWeight:

    def __init__(self, w):
        self.weight = w
        self.length = len(self.weight)
        self.s = sum(self.weight)

        for i in range(1, self.length):
            self.weight[i] += self.weight[i - 1]
            # w[i] += w[i - 1]

    def pickIndex(self):
        l = 0
        r = self.length - 1
        seed = random.randint(1, self.s)
        while l < r:
            mid = (l + r) // 2

            if seed <= self.weight[mid]:
                r = mid
            else:
                l = mid + 1
        return l


rpw = RandomPickWeight([6, 3, 1])
print(rpw)
count0 = 0
count1 = 0
count2 = 0
total = 1000000
for i in range(total):
    temp = rpw.pickIndex()
    if temp == 0:
        count0 += 1
    elif temp == 1:
        count1 += 1
    elif temp == 2:
        count2 += 1

print(count0/total)
print(count1/total)
print(count2/total)
