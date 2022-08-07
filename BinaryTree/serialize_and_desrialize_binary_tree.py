# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from queue import Queue

# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

# All test case not passing


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        q = Queue()
        d1 = {}
        if root is None:
            return str(d1)
        q.put((0, "Ro", root, None))
        while not q.empty():
            level, child_type, node, par = q.get()
            d1[level] = d1.get(level, []) + [(child_type, node.val, par)]
            if node.left:
                q.put((level + 1, "L", node.left, node.val))
            if node.right:
                q.put((level + 1, "R", node.right, node.val))
        print(d1)
        return str(d1)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def find_par(root, val, lvl, level):
            if root is None:
                return None
            elif root.val == val and level == lvl:
                return root
            else:
                lh = find_par(root.left, val, lvl + 1, level)
                rh = find_par(root.right, val, lvl + 1, level)

                if lh is None:
                    return rh
                if rh is None:
                    return lh

                return root

        d1 = eval(data)
        keys = list(d1.keys())
        root = None
        for level in keys:
            children = d1[level]
            for child in children:
                par = find_par(root, child[2], 0, level - 1)
                if par is None:
                    root = TreeNode(child[1])
                else:
                    child_type = child[0]
                    if child_type == "L":
                        par.left = TreeNode(child[1])
                    if child_type == "R":
                        par.right = TreeNode(child[1])

        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
