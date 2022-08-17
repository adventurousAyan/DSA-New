# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# https://leetcode.com/problems/delete-node-in-a-bst/


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def dfs(root, key):
            if root is None:
                return root
            if key < root.val:
                root.left = dfs(root.left, key)
            elif key > root.val:
                root.right = dfs(root.right, key)
            else:
                if root.left is None:
                    return root.right
                elif root.right is None:
                    return root.left
                else:
                    root.val = find_min(root.right)
                    root.right = dfs(root.right, root.val)
            return root

        def find_min(root):
            if root is None:
                return float("inf")

            return min(root.val, find_min(root.left))

        root = dfs(root, key)
        return root
