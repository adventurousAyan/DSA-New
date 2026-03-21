# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# https://leetcode.com/problems/binary-tree-level-order-traversal/?envType=problem-list-v2&envId=binary-tree
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        from collections import deque

       
        if root is None:
            return []
        q = deque()
        q.append(root)
        res = []

        while len(q) > 0:
            ls = []
            for _ in range(len(q)):
                node = q.popleft()
                ls.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(ls)
        return res


        