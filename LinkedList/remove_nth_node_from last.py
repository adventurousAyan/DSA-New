# Definition for singly-linked list.
from typing import Optional

# https://leetcode.com/problems/remove-nth-node-from-end-of-list/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        d1 = {}
        cur = head
        ct = 0
        prev = None
        while cur:
            ct += 1
            d1[ct] = [prev, cur.next]
            prev = cur
            cur = cur.next

        idx = ct - n + 1
        previous = d1[idx][0]
        next = d1[idx][1]
        if not previous:
            head = next
        else:
            previous.next = next
        return head
