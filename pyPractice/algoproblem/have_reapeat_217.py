


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        d = dict()

        for i in nums:
            if d.get(i):
                return True
            else:
                d[i]= 1
        return False

t = [1,2,3,1]

s = Solution()
r = s.containsDuplicate(t)
print(r)