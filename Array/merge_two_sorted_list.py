# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        # print(list1)
        ls = []
        while list1 and list2:
            if list1.val < list2.val:
                ls.append(list1.val)
                list1 = list1.next

            elif list1.val > list2.val:
                ls.append(list2.val)
                list2 = list2.next
            else:
                ls.append(list1.val)
                list1 = list1.next
        while list1:
            ls.append(list1.val)
            list1 = list1.next
        while list2:
            ls.append(list2.val)
            list2 = list2.next

        head = None
        if len(ls) > 0:
            new_list = ListNode()
            head = new_list
            new_list.val = ls[0]
            for i in range(1, len(ls)):
                p = ListNode(ls[i])
                new_list.next = p
                new_list = new_list.next
        return head
