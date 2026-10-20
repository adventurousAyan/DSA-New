# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        dummy = ListNode(0)
        head = dummy
        l1, l2 = list1, list2
        #res = dummy.next
        while l1 and l2:
            if l1.val <= l2.val:
                head.next = ListNode(l1.val)
                l1 = l1.next
            else:
                head.next = ListNode(l2.val)
                l2 = l2.next
            head = head.next

        while l1:
            head.next = ListNode(l1.val)
            l1 = l1.next
            head = head.next
        
        while l2:
            head.next = ListNode(l2.val)
            l2 = l2.next
            head = head.next
           
        return dummy.next
        