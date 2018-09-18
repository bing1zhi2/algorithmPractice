# -*- coding:utf-8 -*-
"""
Given nums [2,7,11,15] target=9
because num[0] + num[1] = 2 + 7
return [0,1]
"""


def twoSum(nums, target):
    """

    :param nums:
    :param target:
    :return:  array
    """
    d = {}
    for i in range(len(nums)):
        res = target - nums[i]
        if res in d:
            return [d[res], i]
        d[nums[i]] = i
