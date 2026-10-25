# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        res = []

        if root is None:
            return []
        
        queue = deque()

        queue.append(root)
       
        while queue:
            ls = []
            q_size = len(queue)
            for _ in range(q_size):
                node = queue.popleft()
                ls.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(ls)
        
        return res