# Definition for singly-linked list.
from typing import Optional

# https://www.youtube.com/watch?v=XVuQxVej6y8
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # Take a dummy node
        dummy = ListNode(0, head)

        # Point nodes
        slow = dummy
        fast = head

        # Iterate till n and move the fast pointer
        for _ in range(n):
            fast = fast.next

        # Now move slo and fast both, till fast is null
        while fast:
            fast = fast.next
            slow = slow.next

        # The moment fast reaches null, slow will be pointing to the prev node to be deleted.
        # Delete the node by pointing slow next to slow next.next
        slow.next = slow.next.next

        # Return dummy.next
        return dummy.next
