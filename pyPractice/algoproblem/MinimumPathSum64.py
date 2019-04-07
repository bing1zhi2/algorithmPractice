"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""
import sys


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        m = len(grid)
        n = len(grid[0])

        d = []
        for i in range(m):
            d.append([0] * n)
        d[0][0] = grid[0][0]

        for i in range(1, len(grid)):
            d[i][0] = d[i - 1][0] + grid[i][0]

        for j in range(1, len(grid[0])):
            d[0][j] = d[0][j - 1] + grid[0][j]

        for i in range(1, m):
            for j in range(1, n):
                d[i][j] = min(d[i - 1][j] + grid[i][j], d[i][j - 1] + grid[i][j])

        return d[-1][-1]

    def min_path(self, grid, i, j):
        if i == 0 and j == 0:
            return grid[0][0]
        else:
            return min(self.min_path(grid, i - 1, j) + grid[i, j], self.min_path(grid, i, j - 1) + grid[i, j])


a = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]
s = Solution()
re = s.minPathSum(a)
print(re)
