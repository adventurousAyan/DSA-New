# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# We can solve it using a brute force by first finding inorder,
# then sort inorder and then again doing a dfs and comparing the inorder values with the node values
# Optimally we can solve this and we have to take three pointers, first, middle and last
# Now the nodes can be adjacent or cannot be adjacent. So if nodes are adjacent,
# there will be only one violation and we can swap middle and first
# When nodes are not adjacent, there can be two violations, first and last and we donot need the middle

# https://leetcode.com/problems/recover-binary-search-tree/
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def dfs(root):
            if root is None:
                return None

            dfs(root.left)

            if self.prev and self.prev.val > root.val:
                if not self.first:
                    self.first = self.prev
                    self.middle = root
                else:
                    self.last = root

            self.prev = root

            dfs(root.right)

        self.prev = None
        self.first = None
        self.middle = None
        self.last = None
        dfs(root)
        if self.last:
            self.first.val, self.last.val = self.last.val, self.first.val
        else:
            self.first.val, self.middle.val = self.middle.val, self.first.val

        return root
