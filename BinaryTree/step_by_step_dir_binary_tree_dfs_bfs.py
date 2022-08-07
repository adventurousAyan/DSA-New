# Definition for a binary tree node.
import collections
from typing import Optional
from queue import Queue

# https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getDirections(
        self, root: Optional[TreeNode], startValue: int, destValue: int
    ) -> str:
        def make_graph(root, par=None):
            if root is None:
                return None
            else:
                lh = make_graph(root.left, root.val)
                rh = make_graph(root.right, root.val)
                d1[root.val].append(("U", par))
                d1[root.val].append(("L", lh))
                d1[root.val].append(("R", rh))
                return root.val

        d1 = collections.defaultdict(list)

        make_graph(root)
        # print(d1)
        node = d1[startValue]
        q = Queue()
        q.put((startValue, node, ""))
        ans = ""
        seen = collections.defaultdict(list)
        while not q.empty():
            par, ls, s = q.get()
            if par == destValue:
                ans = s
                break
            for val in ls:
                diri = val[0]
                nodeval = val[1]
                if nodeval and nodeval not in seen:
                    q.put((nodeval, d1[nodeval], s + diri))
                    seen[par].append(nodeval)
        return ans
