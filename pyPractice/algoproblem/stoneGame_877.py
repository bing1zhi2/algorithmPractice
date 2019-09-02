# -*- coding:utf-8 -*-
# bing1   

# 2019/9/2   

# 15:34   
"""
亚历克斯和李用几堆石子在做游戏。偶数堆石子排成一行，每堆都有正整数颗石子 piles[i] 。

游戏以谁手中的石子最多来决出胜负。石子的总数是奇数，所以没有平局。

亚历克斯和李轮流进行，亚历克斯先开始。 每回合，玩家从行的开始或结束处取走整堆石头。 这种情况一直持续到没有更多的石子堆为止，此时手中石子最多的玩家获胜。

假设亚历克斯和李都发挥出最佳水平，当亚历克斯赢得比赛时返回 true ，当李赢得比赛时返回 false 。

 

示例：

输入：[5,3,4,5]
输出：true
解释：
亚历克斯先开始，只能拿前 5 颗或后 5 颗石子 。
假设他取了前 5 颗，这一行就变成了 [3,4,5] 。
如果李拿走前 3 颗，那么剩下的是 [4,5]，亚历克斯拿走后 5 颗赢得 10 分。
如果李拿走后 5 颗，那么剩下的是 [3,4]，亚历克斯拿走后 4 颗赢得 9 分。
这表明，取前 5 颗石子对亚历克斯来说是一个胜利的举动，所以我们返回 true 。
 

提示：

2 <= piles.length <= 500
piles.length 是偶数。
1 <= piles[i] <= 500
sum(piles) 是奇数。

亚历克斯和李用几堆石子在做游戏。偶数堆石子排成一行，每堆都有正整数颗石子 piles[i] 。

游戏以谁手中的石子最多来决出胜负。石子的总数是奇数，所以没有平局。

亚历克斯和李轮流进行，亚历克斯先开始。 每回合，玩家从行的开始或结束处取走整堆石头。 这种情况一直持续到没有更多的石子堆为止，此时手中石子最多的玩家获胜。

假设亚历克斯和李都发挥出最佳水平，当亚历克斯赢得比赛时返回 true ，当李赢得比赛时返回 false 。

 

示例：

输入：[5,3,4,5]
输出：true
解释：
亚历克斯先开始，只能拿前 5 颗或后 5 颗石子 。
假设他取了前 5 颗，这一行就变成了 [3,4,5] 。
如果李拿走前 3 颗，那么剩下的是 [4,5]，亚历克斯拿走后 5 颗赢得 10 分。
如果李拿走后 5 颗，那么剩下的是 [3,4]，亚历克斯拿走后 4 颗赢得 9 分。
这表明，取前 5 颗石子对亚历克斯来说是一个胜利的举动，所以我们返回 true 。
 

提示：

2 <= piles.length <= 500
piles.length 是偶数。
1 <= piles[i] <= 500
sum(piles) 是奇数。

链接：https://leetcode-cn.com/problems/stone-game

"""
import collections


class StepScore:
    def __init__(self, fir, sec):
        self.fir = fir
        self.sec = sec

    def __repr__(self):
        return 'StepScore(%s,%s)' % self.fir,self.sec


class Solution:
    def stoneGame(self, piles):
        """

        :param piles:
        :return:
        """
        '''
        定义d ，
        d[i][j]  有两个属性(fir,sec)   
        d[i][j].fir 表示对坐标i 到j 先手可以得的分
        d[i][j].sec 表示对坐标i 到j 后手可以得的分
        
        d[1],[1] = (p[1],0) 对角线是基准情况，只有一个数据，先手得全部分
        
        状态转移：
        
        先手时：选择左边  与 右边 得分大的那个是这时的最好选择
        d[i][j].fir = max(p[i] + d[i+1][j].sec, p[j] + d[i][j-1].sec)
        
        后手时：
            if 先手选择左边：
               d[i][j].sec = d[i+1][j].fir
            if 先手选择右边
               d[i][j].sec = d[i][j-1].fir
                         
        '''
        # s = StepScore(0, 0)
        n = len(piles)
        d = [[[0,0] for _ in range(n)] for _ in range(n)]

        for i in range(n):
            d[i][i][0] = piles[i]
            d[i][i][1] = 0

        for k in range(2, n + 1):
            for i in range(n - 1):
                j = k + i - 1
                if j == n:
                    break
                print(i, j)
                left = piles[i] + d[i + 1][j][1]
                right = piles[j] + d[i][j - 1][1]

                if left > right:
                    d[i][j][0] = left
                    d[i][j][1] = d[i + 1][j][0]
                else:
                    d[i][j][0] = right
                    d[i][j][1]  = d[i][j - 1][0]

        res = d[0][n - 1]
        print(res)
        return res[0] - res[1]


s = Solution()
sss = s.stoneGame([3, 9, 1, 2])
print(sss)
