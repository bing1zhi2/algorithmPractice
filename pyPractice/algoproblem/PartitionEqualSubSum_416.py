# -*- coding:utf-8 -*-
"""
Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:

Each of the array element will not exceed 100.
The array size will not exceed 200.


Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
"""

import numpy as np


class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sum_v = 0
        for i in nums:
            sum_v += i

        if sum %2 != 0:
            return False

        target = int(sum_v / 2)
        print(target)



        # 查找数组中有没有加起来等于sum/2 的数，如果可以满足，说明这个可以分成功

        # 相当于0-1背包问题，背包容量有 sum/2

        n = target + 1
        m = len(nums) + 1

        # arr = [False for i in range(n)]
        # dp =[ [False for i in range(n)] ]* m
        dp = [[False for i in range(n)] for i in range(m)]

        dp[0][0] = True

        # print(dp)

        for i in range(m):
            dp[i][0] = True
        for j in range(n):
            dp[0][j] = False

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j]
                if j >= nums[i - 1]:
                    dp[i][j] = dp[i][j] or dp[i - 1][j - nums[i - 1]]

        # print(dp)

        return dp[len(nums)][target]


input = [1, 5, 11, 5]
input = [1,2,3,5]
s = Solution()
result = s.canPartition(input)
print(result)
