from queue import Queue
from typing import List

# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
# stri


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        d1 = {}
        d = 0
        visited = []
        # Find parent
        if root is None:
            return None
        else:
            q = Queue()
            q.put(root)
            d1[root] = None
            while not q.empty():
                item = q.get()
                if item.left:
                    q.put(item.left)
                    d1[item.left] = item
                if item.right:
                    q.put(item.right)
                    d1[item.right] = item
        # Find Target:
        targt = self.findTarget(root, target)
        myq = Queue()

        # Compute nodes at distance k
        visited.append(targt)
        myq.put((0, targt))
        while not myq.empty():
            d, item = myq.get()
            if d == k:
                myq.put((d, item))
                break
            if item.left and item.left not in visited:
                myq.put((d + 1, item.left))
                visited.append(item.left)
            if item.right and item.right not in visited:
                myq.put((d + 1, item.right))
                visited.append(item.right)
            if d1[item] and d1[item] not in visited:
                myq.put((d + 1, d1[item]))
                visited.append(d1[item])

        ls = []
        while not myq.empty():
            d, item = myq.get()
            ls.append(item.val)
        return ls

    def findTarget(self, root: TreeNode, target: TreeNode):
        if root is None:
            return None
        if root == target:
            return root
        else:
            lh = self.findTarget(root.left, target)
            rh = self.findTarget(root.right, target)
            if lh is None:
                return rh
            if rh is None:
                return lh
            return root
