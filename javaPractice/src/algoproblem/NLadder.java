package algoproblem;

/**
 * Created by Administrator on 2018/9/14.
 * @apiNote  N 个楼梯 一次可以上1,2,3  上楼梯的所有可能情况
 */
public class NLadder {
    public static void main(String[] args) {
        int a=10;
        System.out.println(stepNums(a));
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
}
