'''
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:
Given input matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Example 2:
Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
'''


def rotate2(matrix):
    a = matrix[::-1]
    print('a', a)
    b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    b[:] = b[::-1]
    print(b)

    print(matrix[::-1])
    matrix[:] = zip(*matrix[::-1])


def rotate(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """
    """
    [7,8,9]
    [4,5,6],
    [1,2,3],
    
    [7,4,1],
    [8,5,2],
    [9,6,3]
    """
    n = len(matrix)
    # matrix=matrix[::-1]
    matrix.reverse()
    print(matrix)
    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


matrix = [
    [5, 1, 9, 11],
    [2, 4, 8, 10],
    [13, 3, 6, 7],
    [15, 14, 12, 16]
]

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

rotate2(matrix)
print(matrix)
