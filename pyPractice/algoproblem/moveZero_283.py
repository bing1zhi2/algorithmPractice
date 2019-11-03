"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:

必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。
"""


class Solution(object):
    def moveZeroes(self, nums):
        """
        使用先进先出队列。纪录为0的下标，把非零的向前队列中的下标处依次移动
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        temp = []

        for i in range(len(nums)):
            if nums[i] == 0:
                temp.append(i)
            else:
                if len(temp) > 0:
                    idx = temp[0]
                    nums[idx] = nums[i]
                    nums[i] = 0
                    temp = temp[1:]
                    temp.append(i)


a = [0, 1, 0, 3, 12]
s = Solution()
s.moveZeroes(a)
print(a)
