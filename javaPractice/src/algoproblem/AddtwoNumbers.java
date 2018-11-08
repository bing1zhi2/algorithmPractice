package algoproblem;

import java.util.ArrayList;


/**
 * Created by bing1 on 2018/11/7.
 * @author chenhao
 *
 */

class ListNode{
    int val;
    ListNode next;
    ListNode(int val){
        this.val=val;
    }

    @Override
    public String toString() {
        return "ListNode{" +
                "val=" + val +
                ", next=" + next +
                '}';
    }
}
public class AddtwoNumbers {


    public ListNode addTwoNumbers_2(ListNode l1, ListNode l2) {
        ListNode dummyHead = new ListNode(0);
        ListNode p=l1, q=l2, curr=dummyHead;
        int carry = 0;
        while (p != null || q != null) {
            int x= (p !=null)? p.val:0;
            int y= (q !=null)? q.val:0;
            int sum = carry + x + y;
            carry = sum/10;
            curr.next = new ListNode(sum % 10);
            curr = curr.next;
            if(p !=null) p = p.next;
            if(q !=null) q = q.next;

        }
        if(carry>0) {
            curr.next = new ListNode(carry);
        }
        return dummyHead.next;
    }




    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ArrayList<Integer> list = new ArrayList<>();

        ListNode node = null;
        ListNode tempNode;

        System.out.println(l1.next);

        int adv = 0;
        while (l1 != null || l2 !=null ) {
            int a = 10;
            //累加位和 及上次进位
            int l1Val=(l1 == null) ? 0 : l1.val;
            int l2Val=(l2 == null) ? 0 : l2.val;
            int sum = l1Val + l2Val + adv;
            int temp = 0;
            if (sum >= a) {
                temp = sum - a;
                adv=1;
            } else {
                temp = sum;
                adv =0;
            }
            //遍历向后推进
            l1 = (l1 == null) ? l1 : l1.next;
            l2 = (l2 == null) ? l2 : l2.next;
            list.add(temp);
            tempNode= new ListNode(temp);
            if(node==null){
                node= tempNode;
            }else{
                ListNode lastNode=getLastNode(node);
                lastNode.next =tempNode;
            }

        }
        if (adv != 0) {
            list.add(adv);
            tempNode= new ListNode(adv);
            ListNode lastNode=getLastNode(node);
            lastNode.next =tempNode;
        }

        System.out.println(list);


        return node;
    }

    public ListNode getLastNode(ListNode a) {

        while(a.next!=null){
            a = a.next;
        }
        return a ;
    }

    public static void main(String[] args) {
        ListNode a1 = new ListNode(2);
        ListNode a2 = new ListNode(4);
        ListNode a3 = new ListNode(3);
         a1.next = a2;
         a2.next = a3;

        System.out.println(a1);

        ListNode b1 = new ListNode(5);
        ListNode b2 = new ListNode(6);
//        ListNode b3 = new ListNode(4);
        b1.next = b2;
//        b2.next = b3;

        System.out.println(b1);



        AddtwoNumbers addtwoNumbers=new AddtwoNumbers();

        System.out.println("getlast "+addtwoNumbers.getLastNode(a1));

        ListNode r= addtwoNumbers.addTwoNumbers(a1, b1);
        System.out.println(r);


    }
}
