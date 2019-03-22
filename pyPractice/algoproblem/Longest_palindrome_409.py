'''
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
'''


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = dict()
        even_num = 0
        odd_num = 0
        for i in s:
            count = d.get(i, 0)
            count = count + 1
            if count == 2:
                d[i] = 0
                even_num = even_num + 1
                odd_num = odd_num - 1
            else:
                d[i] = count
                odd_num = odd_num + 1
        if odd_num == 0:
            return even_num * 2
        else:
            return even_num * 2 + 1

    def longestPalindrome2(self, s):
        """
        :type s: str
        :rtype: int
        """
        import collections
        odds = sum(v & 1 for v in collections.Counter(s).values())
        center = 0
        if odds != 0:
            center = 1
        return len(s) - odds + center


s = Solution()
num = s.longestPalindrome2("abccccdd")
num = s.longestPalindrome2("bbbb")
print(num)
