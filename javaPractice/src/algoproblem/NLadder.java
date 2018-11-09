package algoproblem;

/**
 * Created by Administrator on 2018/9/14.
 * @apiNote  N 个楼梯 一次可以上1,2,3  上楼梯的所有可能情况
 */
public class NLadder {
    public static void main(String[] args) {
        int a=10;
        System.out.println(stepNums(a));
        System.out.println(stepNums_2(a));
        System.out.println(climbStairs(a));
    }

    public static int stepNums(int ladderNum){
        if(ladderNum<=0){
            return 0;
        }else if(ladderNum==1){
            return 1;
        }else if(ladderNum==2){
            return 2;
        }else if(ladderNum==3){
            return 4;
        }else {
            return stepNums(ladderNum-3)+stepNums(ladderNum-2)+stepNums(ladderNum-1);
        }
    }

    /**
     * 一次上三步时：
     * 使用动态规划
     * @param ladderNum 总梯子数
     * @return 多少种走法
     */
    public static int stepNums_2(int ladderNum){
        int[] dp = new int[ladderNum + 1];
        dp[1] = 1;
        dp[2] = 2;
        dp[3] = 4;


        for (int i = 4; i <= ladderNum; i++) {
            dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1];
        }
        return dp[ladderNum];
    }

    /**
     * 一次最多上两步时
     * 使用动态规划
     * @param n  总梯子数
     * @return 多少种走法
     */
    public static int climbStairs(int n) {
        int first=1;
        int second=2;
        for(int i=3;i<= n; i ++){
            int third= first + second;
            first = second;
            second = third;
        }
        return second;
    }

}
