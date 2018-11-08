# -*- coding:UTF-8 -*-
"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy_head = ListNode(0)
        p = l1
        q = l2
        curr = dummy_head
        carry = 0

        while (p is not None) or (q is not None):
            x = p.val if (p is not None) else 0
            y = q.val if q is not None else 0
            total = carry + x + y
            carry = total // 10
            curr.next = ListNode(total % 10)
            curr = curr.next
            if p is not None:
                p = p.next
            if q is not None:
                q = q.next

        if carry > 0:
            curr.next = ListNode(carry)

        return dummy_head.next


n = ListNode(2)
a1 = ListNode(4)
a2 = ListNode(3)
n.next = a1
a1.next = a2

m = ListNode(5)
a1 = ListNode(6)
a2 = ListNode(4)
m.next = a1
a1.next = a2

a = Solution()
r = a.addTwoNumbers(n, m)
print(r)
