"""
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

Example:

Input:  [1,2,1,3,2,5]
Output: [3,5]
Note:

The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = 0

        for i in range(len(nums)):
            xor = xor ^ nums[i]

        print(xor)
        xor = xor & (-xor)

        res = [0, 0]

        for num in nums:
            if xor & num == 0:
                res[1] = res[1] ^ num
            else:
                res[0] = res[0] ^ num

        return res


b = [1, 2, 1, 3, 2, 5]
s = Solution()
res = s.singleNumber(b)
print(res)
