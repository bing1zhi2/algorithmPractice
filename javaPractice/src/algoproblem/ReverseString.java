package algoproblem;

/**
 * Created by Administrator on 2018/10/19.
 */
public class ReverseString {
    public static void main(String[] args) {

    }
    public String reverseString(String s) {
        char[] chars= s.toCharArray();
        int begin = 0;
        int end = chars.length - 1;
        while (begin < end) {
            char temp = chars[begin];
            chars[begin] = chars[end];
            chars[end] = temp;
            begin++;
            end--;
        }
        return new String(chars);
    }
}
