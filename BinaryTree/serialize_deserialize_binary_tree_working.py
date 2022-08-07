# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from queue import Queue

# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        q = Queue()
        if root is None:
            return ""
        q.put(root)
        s = str(root.val) + ","
        while not q.empty():
            node = q.get()
            if node.left:
                q.put(node.left)
                s += str(node.left.val) + ","
            else:
                s += "#,"
            if node.right:
                q.put(node.right)
                s += str(node.right.val) + ","
            else:
                s += "#,"
        return s

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        root = None
        q = Queue()
        n = len(data)
        data = data.split(",")
        i = 0
        if data[i] == "":
            return None
        root = TreeNode(data[i])
        q.put(root)
        while not q.empty():
            node = q.get()
            if i + 1 < n and data[i + 1] != "#":
                node.left = TreeNode(data[i + 1])
                q.put(node.left)
            if i + 2 < n and data[i + 2] != "#":
                node.right = TreeNode(data[i + 2])
                q.put(node.right)
            i += 2
        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
