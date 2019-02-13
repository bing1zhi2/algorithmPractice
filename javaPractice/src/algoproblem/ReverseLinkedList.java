package algoproblem;

/**
 * Created by bing1 on 2019/2/12.
 */

//Definition for singly-linked list.


public class ReverseLinkedList {

    public ListNode reverseList(ListNode head) {
        ListNode p =head;
        ListNode lastNode =null;

        while(p !=null){
            ListNode temNode=p.next;
            p.next = lastNode;
            lastNode = p;
            p = temNode;

        }
        return lastNode;

    }

    public static void main(String[] args) {
        ListNode node5 = new ListNode(5);

        ListNode node4 = new ListNode(4);
        node4.next=node5;
        ListNode node3 = new ListNode(3);


        node3.next = node4;

        System.out.println(node3);

    }
}
