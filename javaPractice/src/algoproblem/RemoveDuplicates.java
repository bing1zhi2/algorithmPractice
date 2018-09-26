package algoproblem;

import java.util.HashMap;

/**
 * Created by Administrator on 2018/9/26.
 *
 *  problem desc:
 * Given nums = [0,0,1,1,1,2,2,3,3,4],

 Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

 It doesn't matter what values are set beyond the returned length.
 */
public class RemoveDuplicates {
    public static void main(String[] args) {
        removeDuplicates(new int[]{0,0,1,1,1,2,2,3,3,4});
    }
    public static int removeDuplicates(int[] nums){

        return solution1(nums);
    }

    public static int solution1(int[] nums) {
        int rIndex=0;
        HashMap<Integer,Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (!map.containsKey(nums[i])) {
                map.put(nums[i], i);
                nums[rIndex] = nums[i];
                rIndex++;
            }
        }
        return map.size();
    }
}
