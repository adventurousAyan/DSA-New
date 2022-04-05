class Solution:
    # The given root is the root of the Binary Tree
    # Return the root of the generated BST
    def binaryTreeToBST(self, root):
        # code here
        if root is None:
            return None
        else:
            ls = []
            temp = root
            self.inorder(root, ls)
            bst_order = sorted(ls)
            self.i = 0
            self.inorder_bst(temp, bst_order)
            return temp

    def inorder(self, root, ls):
        if root is None:
            return None
        else:
            self.inorder(root.left, ls)
            ls.append(root.data)
            self.inorder(root.right, ls)

    def inorder_bst(self, root, ls):
        if root is None:
            return None
        else:
            self.inorder_bst(root.left, ls)
            root.data = ls[self.i]
            self.i += 1
            self.inorder_bst(root.right, ls)
