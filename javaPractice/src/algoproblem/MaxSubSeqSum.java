package algoproblem;

/**
 * Created by bing1 on 2019/1/22.
 */
public class MaxSubSeqSum {

    public int maxSubArray(int[] nums) {
        int n=nums.length;
        int thisSum=0,maxSum=0;


        for(int i=1;i<n;i++){
            thisSum = thisSum + nums[i];
            if(thisSum>maxSum){
                maxSum = thisSum;
            }else if(thisSum<0){
                thisSum =0;
            }
        }

        return maxSum;
    }
    public int maxSubArray2(int[] nums) {
        int n=nums.length;
        int[] dp = new int[n];
        dp[0] = nums[0];
        int max=dp[0];


        for(int i=1;i<n;i++){
            dp[i]= nums[i]+ ((dp[i-1]>0)?dp[i-1]:0);
            max = Math.max(max, dp[i]);

        }

        return max;
    }

    public static void main(String[] args) {
        int[] nums= new int []{-2,1,-3,4,-1,2,1,-5,4};
//        nums= new int []{-3,-2,0,-1};
        MaxSubSeqSum m=new MaxSubSeqSum();
        int aaa=m.maxSubArray(nums);
         aaa=m.maxSubArray2(nums);
        System.out.println(aaa);

    }

}
