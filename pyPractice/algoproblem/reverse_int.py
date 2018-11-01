# -*- coding:utf-8 -*-
import sys

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        isneg = False
        if x < 0:
            isneg = True
            x = -x

        max_int = 2**31
        max_int_ne = -max_int
        te = max_int / 10
        te1 = max_int_ne /10
        rev = 0
        while x != 0:
            pop = x % 10
            x= int(x/10)

            if rev > te :
                return 0
            elif rev == te:
                if pop > 7:
                    return 0
            elif rev < te1 :
                return 0
            elif rev == te1 :
                if pop < -8:
                    return 0

            rev = rev * 10 + pop

        if isneg:
            rev = -rev
        return rev



a = Solution()
#b = a.reverse(214748364)
#b = a.reverse(6463847412)
b = a.reverse(-123)
print(b)
