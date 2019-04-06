"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.

Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        import sys

        init_v = sys.maxsize
        d = [init_v] * (n+1)
        d[0] = 0

        for i in range(1, n+1):
            min_v = init_v
            j = 1
            while i - j*j >= 0:
                min_v = min(min_v, d[i - j*j] + 1)
                j += 1
            d[i] = min_v

        return d[n]


    def num_squares(self,n):
        if n < 2:
            return n
        lst = []
        i = 1
        while i * i <= n:
            lst.append(i * i)
            i += 1
        cnt = 0
        toCheck = {n}
        while toCheck:
            cnt += 1
            temp = set()
            for x in toCheck:
                for y in lst:
                    if x == y:
                        return cnt
                    if x < y:
                        break
                    temp.add(x - y)
            toCheck = temp

        return cnt





s = Solution()
# re = s.numSquares(3)
# print(re)
re = s.num_squares(12)
print(re)