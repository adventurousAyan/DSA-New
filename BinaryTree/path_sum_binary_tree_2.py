# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# https://leetcode.com/problems/path-sum-ii/


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(root):

            if root is None:
                return None

            self.ls.append(root.val)
            lh = dfs(root.left)
            rh = dfs(root.right)
            if lh is None and rh is None:
                if sum(self.ls) == targetSum:
                    self.res.append(self.ls.copy())
            self.ls.pop()
            return root

        self.ls = []
        self.res = []
        dfs(root)
        return self.res
