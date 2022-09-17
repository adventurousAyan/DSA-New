"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

# https://leetcode.com/problems/copy-list-with-random-pointer/


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":

        cur = head
        front = head
        while cur:
            front = cur.next
            copy = Node(cur.val)
            cur.next = copy
            copy.next = front
            cur = front

        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        cur = head
        dummy = Node(0)
        cur1 = dummy
        while cur:
            cur1.next = cur.next
            cur = cur.next.next
            cur1 = cur1.next
        return dummy.next
