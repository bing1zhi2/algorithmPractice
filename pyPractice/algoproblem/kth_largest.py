'''
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
'''


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        Runtime: 3040 ms, faster than 5.02% of Python online submissions for Kth Largest Element in an Array.
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        N = len(nums)
        for i in range(N):
            for j in range(i+1, N):
                if nums[i] < nums[j]:
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp
            print(i, nums)
            if i == k -1:
                break
        return nums[i]

    def divid(self,nums,left,right):
        base = nums[left]
        while left< right:
            while left < right and nums[right] >= base:
                right = right -1
            nums[left] = nums[right]
            while left < right and nums[left] <= base:
                left = left +1
            nums[right] = nums[left]
        nums[left] = base

        return left


    def quik_sort(self, nums,left,right):
        if left < right:

            base_idx = self.divid(nums,left,right)
            self.quik_sort(nums,left,base_idx-1)
            self.quik_sort(nums,base_idx+1,right)



    def findKthLargest2(self, nums, k):
        """
        Runtime: 3040 ms, faster than 5.02% of Python online submissions for Kth Largest Element in an Array.
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        N = len(nums)
        self.quik_sort(nums,0,N-1)
        print(nums)


        return nums[N -k]


nu = [3,2,1,5,6,4]
a = Solution()
a.findKthLargest(nu,2)
aaa =a.findKthLargest2(nu,2)
print(aaa)
