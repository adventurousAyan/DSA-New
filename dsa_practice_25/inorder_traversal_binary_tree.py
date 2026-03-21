# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# https://leetcode.com/problems/binary-tree-inorder-traversal/?envType=problem-list-v2&envId=binary-tree
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        def inorder(root, ls):
            if root is None:
                return []
            inorder(root.left, ls)
            ls.append(root.val)
            inorder(root.right, ls)
            return ls
        ls = []
        return inorder(root, ls)