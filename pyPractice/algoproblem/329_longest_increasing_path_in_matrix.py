# coding:utf-8
'''
给定一个 m x n 整数矩阵 matrix ，找出其中 最长递增路径 的长度。

对于每个单元格，你可以往上，下，左，右四个方向移动。 你 不能 在 对角线 方向上移动或移动到 边界外（即不允许环绕）。

 

示例 1：


输入：matrix = [ [9,9,4],
                [6,6,8],
                [2,1,1]]
输出：4 
解释：最长递增路径为 [1, 2, 6, 9]。
示例 2：


输入：matrix = [[3,4,5],[3,2,6],[2,2,1]]
输出：4 
解释：最长递增路径是 [3, 4, 5, 6]。注意不允许在对角线方向上移动。
示例 3：

输入：matrix = [[1]]
输出：1
 

提示：

m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
0 <= matrix[i][j] <= 231 - 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-increasing-path-in-a-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
import collections
from functools import lru_cache


class Solution:

    # def __init__(self):
    #     self.steps = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

    #     rows, columns = len(matrix), len(matrix[0])
    #     memory = [[0] * columns for _ in range(rows)]
    #     ans = 0
    #     for i in range(rows):
    #         for j in range(columns):
    #             print("--------------i,j:{},{}".format(i, j))
    #             ans = max(ans, self.dfs(matrix, memory, i, j))
    #             print(memory)
    #     print(ans)

    # # @lru_cache(None)
    # def dfs(self, matrix: List[List[int]], memory: List[List[int]], curr_row, curr_column) -> int:
    #     rows, columns = len(matrix), len(matrix[0])
    #     if memory[curr_row][curr_column] != 0:
    #         return memory[curr_row][curr_column]

    #     memory[curr_row][curr_column] += 1
    #     print("curr_row:{},curr_column:{},memory[{},{}]:{}".format(curr_row, curr_column, curr_row, curr_column, memory[curr_row][curr_column]))

    #     for dx, dy in self.steps:
    #         new_row, new_column = curr_row + dx, curr_column + dy
    #         if dx == 0:
    #             pass
    #         elif dx < 0:
    #             print("上")
    #         else:
    #             print("下")
    #         if dy == 0:
    #             pass
    #         elif dy < 0:
    #             print("左")
    #         else:
    #             print("右")

    #         if 0 <= new_row < rows and 0 <= new_column < columns and matrix[new_row][new_column] > matrix[curr_row][curr_column]:
    #             # memory[curr_row][curr_column] = max(memory[curr_row][curr_column], self.dfs(matrix, memory, new_row, new_column) + 1)
    #             print("new_row, new_column:{},{}".format(new_row, new_column))
    #             a = memory[curr_row][curr_column]
    #             b = self.dfs(matrix, memory, new_row, new_column) + 1
    #             memory[curr_row][curr_column] = max(a, b)
    #             print("memory[{},{}]:{}".format(curr_row, curr_column, memory[curr_row][curr_column]))

    #     return memory[curr_row][curr_column]

    DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0

        rows, columns = len(matrix), len(matrix[0])
        outdegrees = [[0] * columns for _ in range(rows)]
        queue = collections.deque()
        for i in range(rows):
            for j in range(columns):
                for dx, dy in Solution.DIRS:
                    newRow, newColumn = i + dx, j + dy
                    if 0 <= newRow < rows and 0 <= newColumn < columns and matrix[newRow][newColumn] > matrix[i][j]:
                        outdegrees[i][j] += 1
                if outdegrees[i][j] == 0:
                    queue.append((i, j))

        ans = 0
        while queue:
            ans += 1
            size = len(queue)
            for _ in range(size):
                row, column = queue.popleft()

                for dx, dy in Solution.DIRS:
                    newRow, newColumn = row + dx, column + dy
                    if 0 <= newRow < rows and 0 <= newColumn < columns and matrix[newRow][newColumn] < matrix[row][column]:
                        outdegrees[newRow][newColumn] -= 1
                        if outdegrees[newRow][newColumn] == 0:
                            print(newRow, newColumn)
                            queue.append((newRow, newColumn))

        return ans


matrix = [[1, 9, 4], [2, 6, 8], [6, 9, 1]]

matrix = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
'''
matrix = [      [9,9,4],
                [6,6,8],
                [2,1,1]]
'''
solution = Solution()
b = solution.longestIncreasingPath(matrix)
print(b)