"""
Given an integer, return its base 7 string representation.

Example 1:
Input: 100
Output: "202"
Example 2:
Input: -7
Output: "-10"
Note: The input will be in range of [-1e7, 1e7].
"""


class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"

        num_copy = abs(num)
        res = ''

        while num_copy:
            tmp = num_copy // 7
            com = num_copy % 7
            res = str(com) + res
            num_copy = tmp

        if num < 0:
            return "-" + res
        else:
            return res

        #
        # a = num  // 7
        # com = num  % 7
        # res.append(com)
        #
        # print(a, res)
        #
        # b = a // 7
        # com = a % 7
        # res.append(com)
        #
        # print(res)


s = Solution()
s.convertToBase7(7)
