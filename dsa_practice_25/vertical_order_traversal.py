# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/?envType=problem-list-v2&envId=binary-tree
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        from collections import deque

        if root is None:
            return None
        q = deque()
        vlvl = 0
        hlvl = 0
        d = defaultdict(list)
        q.append((root, hlvl, vlvl))

        while len(q) > 0:
            for _ in range(len(q)):
                node, hlvl, vlvl = q.popleft()
                d[(hlvl, vlvl)].append(node.val)
                if node.left:
                    q.append((node.left, hlvl + 1, vlvl - 1))
                if node.right:
                    q.append((node.right, hlvl+1, vlvl + 1))
        d1 = {}

        for key, value in d.items():
            if len(value) > 1:
                value.sort()
            hlvl, vlvl = key
            if d1.get(vlvl) is None:
                d1[vlvl] = value
            else:
                d1[vlvl].extend(value)

        d2 = dict(sorted(d1.items(), key = lambda x: x[0]))  
        return list(d2.values())
