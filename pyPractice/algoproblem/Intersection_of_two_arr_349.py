"""
给定两个数组，编写一个函数来计算它们的交集。

示例 1:

输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2]
示例 2:

输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出: [9,4]
说明:

输出结果中的每个元素一定是唯一的。
我们可以不考虑输出结果的顺序。


"""


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        此解法很幼稚 官方答案说
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d = dict()
        d2 = {}
        for i in nums1:
            d[i] = 1

        for i in nums2:
            if d.get(i):
                d2[i] = 1
        return list(d2.keys())

    def intersection2(self, nums1, nums2):
        """
        内置函数
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        n1 = set(nums1)
        n2 = set(nums2)

        return list(n1 & n2)

    def set_intersection(self, set1, set2):
        return [x for x in set1 if x in set2]

    def intersection3(self, nums1, nums2):
        """
        把小的一边进行比较
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set1 = set(nums1)
        set2 = set(nums2)

        if len(set1) < len(set2):
            return self.set_intersection(set1, set2)
        else:
            return self.set_intersection(set2, set1)


nums1 = [1, 2, 2, 1]
nums2 = [3, 2, 2]

s = Solution()
r = s.intersection3(nums1, nums2)
print(r)
