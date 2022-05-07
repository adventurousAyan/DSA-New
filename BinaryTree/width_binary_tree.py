# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
from queue import Queue
from typing import Optional
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        q = Queue()
        q.put((0,root))
        maxno = float('-inf')
        while not q.empty():
            n = q.qsize()
            ls = []
            for i in range(n):
                idx, item = q.get()
                ls.append(idx)
                if item.left:
                    q.put((2*idx + 1,item.left))
                if item.right:
                    q.put((2*idx + 2,item.right))
                maxno = max(maxno, ls[-1]-ls[0]+1)
        return maxno