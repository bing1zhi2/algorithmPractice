package algoproblem;

/**
 * Created by bing1 on 2019/1/25.
 */
public class LongestPalindrome {

    public String longestPalindrome1(String s) {
        if(s==null ||s.length()<1){
            return "";
        }
        int start = 0, end = 0;
        for(int i= 0 ; i< s.length(); i++) {
            int len1 = expandAroundCenter(s, i, i);
            int len2 = expandAroundCenter(s, i, i+1);
            int len = Math.max(len1, len2);
            if (len > end - start) {
                start = i - (len - 1) / 2;
                end = i + len / 2;
            }

        }
        return s.substring(start, end + 1);

    }

    private int expandAroundCenter(String s, int left, int right) {
        int L = left, R = right;
        while (L >= 0 && R < s.length() && s.charAt(L) == s.charAt(R)) {
            L--;
            R++;
        }
        return R - L - 1;
    }

    public int extendCenter(String s,int l,int r){
        int left= l,right =r;
        while(left>=0 && right<s.length() ){
            char a= s.charAt(left);
            char b= s.charAt(right);
            if(a==b){
                left--;
                right++;
            }else{
                break;
            }
        }
        return right-left-1;
    }



    public static void main(String[] args) {
        LongestPalindrome lp =new LongestPalindrome();


        int result =lp.expandAroundCenter("abadcedec", 1, 1);
        int result3 = lp.extendCenter("abadcedec", 1, 1);
        int result2 =lp.expandAroundCenter("abadcedec", 1, 2);
        System.out.println(result);
        System.out.println(result2);
    }


}
