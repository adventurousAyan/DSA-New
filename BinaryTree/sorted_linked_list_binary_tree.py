# Definition for singly-linked list.
from typing import Optional

# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def find_middle(head):
            slow = head
            fast = head
            prev = head
            while fast.next and fast.next.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            prev.next = None
            return slow

        def build_tree(head):
            if head is None:
                return None
            if head.next and head.next.next:
                mid = find_middle(head)
                root = TreeNode(mid.val)

            elif head.next:
                mid = head.next
                root = TreeNode(mid.val)
                head.next = None
            elif head:
                return TreeNode(head.val)

            root.left = build_tree(head)
            root.right = build_tree(mid.next)

            return root

        rt = build_tree(head)
        return rt
