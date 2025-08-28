# Definition for singly-linked list.

# https://leetcode.com/problems/add-two-numbers/description/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy2 = ListNode()
        tmp = dummy2
        carry = 0
        while l1 and l2:
            s1 = (l1.val + l2.val + carry) % 10 
            carry = (l1.val + l2.val + carry) // 10
            tmp.next = ListNode(s1)
            l1 = l1.next
            l2 = l2.next
            tmp = tmp.next
        
        while l1:
            s1 = (l1.val + carry) % 10 
            carry = (l1.val + carry) // 10
            tmp.next = ListNode(s1)
            l1 = l1.next
            tmp = tmp.next
        
        while l2:
            s1 = (l2.val + carry) % 10 
            carry = (l2.val + carry) // 10
            tmp.next = ListNode(s1)
            l2 = l2.next
            tmp = tmp.next
        if carry > 0:
            tmp.next = ListNode(carry)
        return dummy2.next
        
        

        