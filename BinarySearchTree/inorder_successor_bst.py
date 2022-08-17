# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# https://leetcode.com/problems/inorder-successor-in-bst/


class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        def dfs(root, p):
            if root is None:
                return None
            if root.val > p.val:
                self.inordersucc = root
                return dfs(root.left, p)
            return dfs(root.right, p)

        self.inordersucc = None
        dfs(root, p)
        return self.inordersucc
