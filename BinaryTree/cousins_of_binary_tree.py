# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# https://leetcode.com/problems/cousins-in-binary-tree/


from typing import Optional


class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        def dfs(root, x, h=0, par=-1):
            if root is None:
                return None
            elif root.val == x:
                return (par, h)
            else:
                lh = dfs(root.left, x, h + 1, root.val)
                rh = dfs(root.right, x, h + 1, root.val)

                if lh is None:
                    return rh
                elif rh is None:
                    return lh
                return root

        t1, h1 = dfs(root, x)
        t2, h2 = dfs(root, y)
        if h1 == h2 and t1 != t2:
            return True
        return False
