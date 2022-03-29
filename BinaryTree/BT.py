class BT:
    def __init__(self) -> None:
        self.root = None
        self.ls = []

    def inorder(self):
        if self.root:
            return self.root.inorder(self.root, self.ls)


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def inorder(self, curnode, ls):
        if curnode.left:
            self.left.inorder(self.left, ls)
        print(self.data)
        ls.append(self.data)
        if curnode.right:
            self.right.inorder(self.right, ls)


bt = BT()
bt.root = Node(1)
bt.root.left = Node(2)
bt.root.left.left = Node(4)
bt.root.right = Node(3)

bt.inorder()
bt.ls.sort()
