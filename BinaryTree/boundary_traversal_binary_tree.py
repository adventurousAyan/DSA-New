# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# https://leetcode.com/problems/boundary-of-binary-tree/


class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        def is_leaf(root):
            if root is None:
                return False
            if root.left or root.right:
                return False
            return True

        def find_left(root):
            if root is None or is_leaf(root):
                return
            self.ls.append(root.val)
            if root.left:
                find_left(root.left)
            else:
                find_left(root.right)

        def in_order(root):
            if root is None:
                return
            if is_leaf(root):
                self.ls.append(root.val)
                return
            in_order(root.left)
            in_order(root.right)

        def find_right(root):
            if root is None or is_leaf(root):
                return
            self.l1.append(root.val)
            if root.right:
                find_right(root.right)
            else:
                find_right(root.left)

        self.ls = []
        self.l1 = []
        if not is_leaf(root):
            self.ls.append(root.val)
        find_left(root.left)
        in_order(root)
        find_right(root.right)

        while len(self.l1) > 0:
            self.ls.append(self.l1.pop())

        return self.ls
