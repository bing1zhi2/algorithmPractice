from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1
        r = -1
        while left <= right:
            mid =  (left + right) // 2
            if target < nums[mid]:
                right = mid - 1
            elif target == nums[mid]:
                r = mid
                right = -1
            else:
                left = mid + 1
        return r


nums =[-1,0,3,5,9,12]
target = 2

s = Solution()
re = s.search(nums, target)
print(re)