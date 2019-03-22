# -*- coding:utf-8 -*-
"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2

摩尔投票算法是基于这个事实：
每次从序列里选择两个不相同的数字删除掉（或称为“抵消”），
最后剩下一个数字或几个相同的数字，就是出现次数大于总数一半的那个


输入：{1,2,1,3,1,1,2,1,5}
从第一个数字1开始，我们想要把它和一个不是1的数字一起从数组里抵消掉，但是目前我们只扫描了一个1，所以暂时无法抵消它，
把它加入到array，array变成了{1}，result由于没有抵消任何元素所以还是原数组{1,2,1,3,1,1,2,1,5}。
然后继续扫描第二个数，是2，我们可以把它和一个不是2的数字抵消掉了，因为我们之前扫描到一个1，所以array变成了{},result变成了{1,3,1,1,2,1,5}
继续扫描第三个数1，无法抵消，于是array变成了{1},result还是{1,3,1,1,2,1,5};
接下来扫描到3,可以将3和array数组里面的1抵消,于是array变成了{},result变成了{1,1,2,1,5}
接下来扫描到1，此时array为空，所以无法抵消这个1，array变成了{1},result还是{1,1,2,1,5}
接下来扫描到1，此时虽然array不为空，但是array里也是1，所以还是无法抵消，把它也加入这个array,于是array变成了{1,1}（
其实到这我们可以发现，array里面只可能同时存在一种数，因为只有array为空或当前扫描到的数和array里的数字相同时才把这个数字放入array）,
result还是{1,1,2,1,5}接下来扫描到2，把它和一个1抵消掉，至于抵消哪一个1，无所谓，array变成了{1},result是{1,1,5}
接下来扫描到1，不能抵消，array变成了{1,1}，result{1,1,5}
接下来扫描到5，可以将5和一个1抵消，array变成了{1},result变成了{1}
至此扫描完成了数组里的所有数，result里剩了1，所以1就是大于一半的数组。
"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import collections
        counter = collections.Counter(nums)
        n_2 = len(nums) // 2

        for key in counter.keys():
            value = counter.get(key)
            if value > n_2:
                return key

    def majorityElement2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if count == 0:
                count += 1
                temp = nums[i]
            elif temp == nums[i]:
                count += 1
            else:
                count -= 1
        return temp




s = Solution()
a =  [2,2,1,1,1,2,2]
a =  [3,3,4]
result = s.majorityElement2(a)
print(result)