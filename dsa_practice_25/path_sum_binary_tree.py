# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:


        if root is None:
            return False
        if self.isLeaf(root) and targetSum == root.val:
            return True
        lsum = self.hasPathSum(root.left, targetSum -root.val)
        rsum = self.hasPathSum(root.right, targetSum - root.val)
        return lsum | rsum
    
    def isLeaf(self, root):
        return root.left is None and root.right is None

# https://leetcode.com/problems/path-sum/?envType=problem-list-v2&envId=binary-tree