# Definition for singly-linked list.
from typing import Optional

# https://leetcode.com/problems/add-two-numbers/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        dummy = ListNode()
        cur = dummy
        carry = 0

        while l1 and l2:
            val = (l1.val + l2.val + carry) % 10
            cur.next = ListNode(val)
            carry = (l1.val + l2.val + carry) // 10
            l1 = l1.next
            l2 = l2.next
            cur = cur.next

        while l2:
            val = (l2.val + carry) % 10
            cur.next = ListNode(val)
            carry = (l2.val + carry) // 10
            l2 = l2.next
            cur = cur.next

        while l1:
            val = (l1.val + carry) % 10
            cur.next = ListNode(val)
            carry = (l1.val + carry) // 10
            l1 = l1.next
            cur = cur.next

        if carry != 0:
            cur.next = ListNode(carry)
            cur = cur.next

        return dummy.next
