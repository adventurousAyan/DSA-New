# User function Template for python3
from queue import Queue
from collections import OrderedDict


class Solution:
    def bottomView(self, root):
        # code here
        def dfs(root, link):
            if root is None:
                return None
            while not q.empty():
                root, link = q.get()
                if root:
                    d1[link] = root.data
                if root.left:
                    q.put((root.left, link - 1))
                if root.right:
                    q.put((root.right, link + 1))

        q = Queue()
        q.put((root, 0))
        d1 = {}
        dfs(root, 0)
        d1 = sorted(d1.items(), key=lambda x: x[0])
        return [x[1] for x in d1]
