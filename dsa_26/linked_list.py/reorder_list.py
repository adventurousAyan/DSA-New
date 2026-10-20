# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        def find_mid(head):
            slow, fast = head, head

            while fast and fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
                
            return slow

        def reverse_list(head):
            prev, curr = None, head

            while curr:
                nxt = curr.next 
                curr.next = prev
                prev = curr
                curr = nxt
            return prev


        mid = find_mid(head)
        second = mid.next
        # split the list into two halves
        mid.next = None
        # reverse the second half
        rev = reverse_list(second)
        # merge the two halves
        curr = head
        while rev:
            tmp, revtmp = curr.next, rev.next
            curr.next = rev
            rev.next = tmp
            curr, rev = tmp, revtmp


        
        