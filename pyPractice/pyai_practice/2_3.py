'''
在经典汉诺塔问题中，有 3 根柱子及 N 个不同大小的穿孔圆盘，盘子可以滑入任意一根柱子。一开始，所有盘子自上而下按升序依次套在第一根柱子上(即每一个盘子只能放在更大的盘子上面)。移动圆盘时受到以下限制:
(1) 每次只能移动一个盘子;
(2) 盘子只能从柱子顶端滑出移到下一根柱子;
(3) 盘子只能叠在比它大的盘子上。

请编写程序，用栈将所有盘子从第一根柱子移到最后一根柱子。

你需要原地修改栈。

此问题不问步数，只做移动。
'''
from typing import List


class Solution:

    def hanota(self, A: List[int], B: List[int], C: List[int]) -> None:
        """
        Do not return anything, modify C in-place instead.
        """

        # 移动 n-1个盘到B，

        # 移动最后一个盘到C

        # 把n-1个盘B移动到C

        self.move(len(A), A, B, C)

    def move(self, n, A: List[int], B: List[int], C: List[int]) -> None:

        if n == 1:
            C.append(A.pop())
            return
        else:
            self.move(n - 1, A, C, B)
            C.append(A.pop())
            self.move(n - 1, B, A, C)


class Solution2:

    def hanota(self, A: List[int], B: List[int], C: List[int]) -> int:
        """
        计算步数  封 闭 形 式 的 解．为 Tn =  2^n - 1 by 具体数学
        """

        # 移动 n-1个盘到B，

        # 移动最后一个盘到C

        # 把n-1个盘B移动到C

        return self.move(len(A), A, B, C)

    def move(self, n, A: List[int], B: List[int], C: List[int]) -> int:

        if n == 1:
            C.append(A.pop())
            return 1
        else:
            first_setp_nums = self.move(n - 1, A, C, B)
            C.append(A.pop())
            last_step_nums = self.move(n - 1, B, A, C)
            return first_setp_nums + 1 + last_step_nums


s = Solution2()

aaa = s.hanota([4, 3, 2, 1, 0], [], [])

print(aaa)
