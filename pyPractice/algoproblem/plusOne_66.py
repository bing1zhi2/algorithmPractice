"""
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:

输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
示例 2:

输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。


"""


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        length = len(digits)
        queue = [1]

        for i in range(length - 1, -1, -1):
            high = queue.pop()
            s = high + digits[i]
            if s < 10:
                digits[i] = s
                return digits
            elif s == 10:
                digits[i] = 0
                queue.append(1)
            else:
                digits[i] = s - 10
                queue.append(1)
        if len(queue) > 0:
            digits.insert(0, 1)
        return digits


a = [1, 9]
s = Solution()
a1 = s.plusOne(a)
print(a1)
