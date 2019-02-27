class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


'''
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
'''
class Solution:
    def reverseList(self, head: 'ListNode') -> 'ListNode':
        p = head
        last_node = None

        while(p):
            temp = p.next
            p.next = last_node
            last_node = p
            p = temp

        return last_node



a = ListNode(5)
b = ListNode(4)
c = ListNode(3)