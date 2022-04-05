# https://practice.geeksforgeeks.org/problems/normal-bst-to-balanced-bst/1#
class Node:
    def __init__(self, val):
        self.left = None
        self.data = val
        self.right = None


class Solution:
    def buildBalancedTree(self, root):
        # code here
        if root is None:
            return None
        else:
            ls = []
            self.inorder(root, ls)
            self.i = 0
            return self.build_bst(ls)

    def inorder(self, root, ls):
        if root is None:
            return None
        else:
            self.inorder(root.left, ls)
            ls.append(root.data)
            self.inorder(root.right, ls)

    def build_bst(self, ls, root=None):
        if len(ls) == 0:
            return None
        if len(ls) == 1:
            return Node(ls[0])
        else:
            start = 0
            end = len(ls) - 1
            mid = start + (end - start) // 2
            root = Node(ls[mid])
            root.left = self.build_bst(ls[:mid], root)
            root.right = self.build_bst(ls[mid + 1 :], root)

        return root
