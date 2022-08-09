# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# https://leetcode.com/problems/kth-smallest-element-in-a-bst/


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(root):
            if root is None:
                return
            dfs(root.left)
            self.k1 -= 1
            if self.k1 == 0:
                self.ans = root.val
            dfs(root.right)

        self.k1 = k
        self.ans = 0
        dfs(root)
        return self.ans
