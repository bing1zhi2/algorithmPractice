# -*- coding:utf-8 -*-
"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
Note:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?
"""


class Solution(object):
    def rotate(self, nums, k):
        """  效率太低
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            temp = nums[len(nums) - 1]
            for n in range(len(nums) - 1, 0, -1):
                nums[n] = nums[n - 1]
            nums[0] = temp
            print(nums)

    def rotate2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        s = l - k
        nums[:] = nums[s:] + nums[:s]

    def rotate3(self, nums, k):
        """
        1, 2, 3, 4, 5, 6, 7
        使用反转的方法

        reverse
        4321 765
        5671234
        :param nums:
        :param k:
        :return:
        """
        pass

    def rotate4(self, nums, k):
        """
        1, 2, 3, 4, 5, 6, 7

        1, 2, 3, 4, 5, 6

        :param nums:
        :param k:
        :return:
        """
        l = len(nums)
        k = k % l  # 如果k小于数组长度，则值不变。否则换算成对应的相同结果的k

        start = 0
        count = 0  # 计录移动多少数字了，全移动一次就完成了

        while count < l:

            current = start
            pre_v = nums[start]

            # do while  ，先do 一遍
            nest = (current + k) % l
            temp = nums[nest]
            nums[nest] = pre_v
            current = nest
            pre_v = temp
            count += 1

            while current != start:
                nest = (current + k) % l
                temp = nums[nest]
                nums[nest] = pre_v
                current = nest
                pre_v = temp
                count += 1

            start += 1  # 对于n%k=0 需要从+1位置开始计算一次，直到移动次数总共为数组长度才把所有的移动完成


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

s = Solution()
bbb = s.rotate4(nums, k=3)
print(nums)
