'''
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.
'''
from collections import Counter


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        print(len(s),len(t))
        if len(s) == len(t):
            counter = Counter(s)
            counter2 = Counter(t)
            flag = True
            for i in counter:
                if counter.get(i) != counter2.get(i):
                    flag = False
            return flag
        else:
            return False



s = Solution()
s.isAnagram("sdfa","afds")