# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None:
            return None
        else:
            cur1 = head
            cur2 = head.next
            cur1.next = None
            reversed_list = cur1

            while cur2 != None:
                tmp = cur2
                cur2 = cur2.next
                tmp.next = reversed_list
                reversed_list = tmp
        return reversed_list
