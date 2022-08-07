import heapq
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        ListNode.__lt__ = lambda self, other: self.val < other.val

        minq = []
        for ls in lists:
            if ls:
                heapq.heappush(minq, (ls.val, ls))

        head = None
        while len(minq) > 0:
            val, node = heapq.heappop(minq)
            if head is None:
                head = ListNode(val)
                cur = head
            else:
                if cur:
                    cur.next = ListNode(val)
                    cur = cur.next
            if node.next:
                heapq.heappush(minq, (node.next.val, node.next))
        return head
