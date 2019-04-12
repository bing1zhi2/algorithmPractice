# -*- coding:utf-8 -*-
"""
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.

"""


class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.sum_list = nums + [1]
        for i in range(len(nums)):
            self.sum_list[i+1] = self.sum_list[i] + nums[i]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """

        return self.sum_list[j +1] - self.sum_list[i]


# Your NumArray object will be instantiated and called as such:
nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)
param_1 = obj.sumRange(2,5)
print(param_1)