# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
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
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
            res.append(ls[0])
        
        return res
        