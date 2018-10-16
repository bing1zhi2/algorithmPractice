package algoproblem;

import java.util.*;

/**
 * Created by Administrator on 2018/10/16.
 * Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

 An input string is valid if:

 Open brackets must be closed by the same type of brackets.
 Open brackets must be closed in the correct order.
 Note that an empty string is also considered valid.
 */
public class IsValid {

    public static void main(String[] args) {
        IsValid isValid=new IsValid();
        boolean result=false;

//        result=isValid.isValid("()[]{}");
//        result=isValid.isValid("()");
//        result=isValid.isValid("(]");
//        result=isValid.isValid("([)]");
        result=isValid.isValid("{[]}");
        System.out.println(result);
    }

    /**
     * 5ms  beats 98%
     * @param s
     * @return
     */
    public boolean isValid(String s) {
        boolean isV=true;
        Map<String,String> bmap = new HashMap<>();
        bmap.put("(",")");
        bmap.put("{","}");
        bmap.put("[", "]");
        LinkedList<String> stack= new LinkedList<>();

        char[] chars=s.toCharArray();
        for(int i =0 ; i< chars.length;i++){
            char a= chars[i];
            String astr=String.valueOf(a);
            if (bmap.containsKey(astr)) {
                stack.addFirst(astr);
            }else {
                if(stack.size()>0){
                    String v = stack.removeFirst();
                    String ss=bmap.get(v);
                    if (astr.equals(ss)) {
                    } else {
                        isV = false;
                        break;
                    }
                }else{
                    isV=false;
                    break;
                }
            }
        }
        if(stack.size()!=0){
            isV=false;
        }
        return isV;
    }


    public boolean isValid2(String s) {
        Stack<Character> stack = new Stack<Character>();
        for (char c : s.toCharArray()) {
            if (c == '(')
                stack.push(')');
            else if (c == '{')
                stack.push('}');
            else if (c == '[')
                stack.push(']');
            else if (stack.isEmpty() || stack.pop() != c){
                return false;
            }

        }
        return stack.isEmpty();
    }

}
