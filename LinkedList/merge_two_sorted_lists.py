# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# https://leetcode.com/problems/merge-two-sorted-lists/


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        dummy = ListNode()
        cur = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = ListNode(list1.val)
                list1 = list1.next
            elif list1.val > list2.val:
                cur.next = ListNode(list2.val)
                list2 = list2.next

            cur = cur.next
        # print(cur)

        while list1:
            cur.next = ListNode(list1.val)
            list1 = list1.next
            cur = cur.next

        while list2:
            cur.next = ListNode(list2.val)
            list2 = list2.next
            cur = cur.next

        return dummy.next
