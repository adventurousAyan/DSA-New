# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        q = deque()

        q.append(root)

        ls = []
        while len(q) > 0:
            su = 0
            size = len(q)
            for _ in range(size):
                root = q.popleft()
                su += root.val
                if root.left:
                    q.append(root.left)
                if root.right:
                    q.append(root.right)
            ls.append(su / size)
        return ls
