# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional

# https://leetcode.com/problems/find-duplicate-subtrees/


class Solution:
    def findDuplicateSubtrees(
        self, root: Optional[TreeNode]
    ) -> List[Optional[TreeNode]]:
        def dfs(root):

            if root is None:
                return "#"
            else:
                lh = dfs(root.left)
                rh = dfs(root.right)

                s = ",".join([str(root.val), lh, rh])
                if s in d1:
                    d1[s] += 1
                    if d1[s] == 2:
                        ls.append(root)
                else:
                    d1[s] = 1

                return s

        d1, ls = {}, []
        dfs(root)
        return ls
