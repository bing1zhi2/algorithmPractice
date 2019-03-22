'''
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
Note:
You may assume k is always valid, 1 ≤ k ≤ n2
'''


class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])
        lo = matrix[0][0]
        hi = matrix[m-1][n-1] + 1

        while(lo < hi):
            mid = lo + int((hi -lo)/2)
            count =0
            j = n-1
            for i in range(m):
                while j >= 0 and matrix[i][j] > mid:
                    j = j - 1
                count = count + (j+1)

            if count < k:
                lo = mid +1
            else:
                hi = mid

        return lo


s = Solution()
a = [[1,5,9],
     [10,11,13],
     [12,13,15]]
# a = [[1,2,4],
#      [1,3,5],
#      [1,3,6],
#      ]

aa =s.kthSmallest(a,8)
print(aa)