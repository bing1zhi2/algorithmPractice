# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next

a0 = ListNode(0)
a1 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(4)

a0.next = a1
a1.next = a2
a2.next = a3


b0 = ListNode(0)
b1 = ListNode(1)
b2 = ListNode(3)
b3 = ListNode(4)

b0.next = b1
b1.next = b2
b2.next = b3

solu =  Solution()
result = solu.mergeTwoLists(a0.next,b0.next)

while result:
    print(result.val)
    result = result.next

