# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:



        def balanced_bt(root):
            if root is None:
                return 0

            lh = balanced_bt(root.left)
            rh = balanced_bt(root.right)

            if abs(rh-lh) > 1:
                self.res = False

            return 1 + max(lh, rh)
        
        self.res = True

        balanced_bt(root)
        return self.res
        