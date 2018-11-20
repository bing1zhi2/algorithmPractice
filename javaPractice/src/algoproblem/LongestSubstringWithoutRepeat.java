package algoproblem;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

/**
 * Created by bing1 on 2018/11/20.
 */
public class LongestSubstringWithoutRepeat {
    public int lengthOfLongestSubstring(String s) {

        Map<Character, Integer> map = new HashMap<>();


        int maxLength=0;

        if( !"".equals(s)){
            for(int rightIndex =0,leftIndex=0; rightIndex < s.length();rightIndex++){
                char a = s.charAt(rightIndex);
                System.out.println("rightIndex:"+ rightIndex +" "+ a );

                if (map.containsKey(a)) {
                    leftIndex = Math.max(map.get(a), leftIndex);
                }

                maxLength =  Math.max(maxLength,rightIndex -leftIndex +1);
                map.put(a,rightIndex+1);
     ;
            }
        }

        return maxLength;
    }
    public static int lengthOfLongestSubstring2(String s) {
        int n = s.length();
        Set<Character> set = new HashSet<>();
        int ans = 0, i = 0, j = 0;
        while (i < n && j < n) {
            // try to extend the range [i, j]
            System.out.println("i:"+s.charAt(j));
            if (!set.contains(s.charAt(j))){
                set.add(s.charAt(j++));
                ans = Math.max(ans, j - i);
            }
            else {
                set.remove(s.charAt(i++));
            }
            System.out.println(set);
        }
        return ans;
    }

    public static void main(String[] args) {
//        String str = "dvdf";
//        int i=0;
//        System.out.println(str.charAt(i++));
//        System.out.println(i);
//        int r = lengthOfLongestSubstring2(str);
//        System.out.println(r);


        LongestSubstringWithoutRepeat lon=new LongestSubstringWithoutRepeat();
        int result = lon.lengthOfLongestSubstring("dvdf");
        System.out.println(result);
    }
}
