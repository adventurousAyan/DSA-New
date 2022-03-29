class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            self.root.insert(data)
        else:
            self.root = Node(data)

    def find(self, data):
        if self.root:
            return self.root.find(data)
        return False

    def inorder(self):
        if self.root:
            return self.root.inorder(self.root)

    def height(self):
        if self.root:
            return self.root.height(self.root)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data == data:
            raise Exception("Data Already exist within tree")
        elif self.data > data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = Node(data)
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = Node(data)

    def find(self, data):
        if data == self.data:
            return True
        elif data < self.data and self.left:
            return self.left.find(data)
        elif data > self.data and self.right:
            return self.right.find(data)
        return False

    def inorder(self, curnode):
        if curnode:
            self.left.inorder(self.left)
            print(self.data)
            self.right.inorder(self.right)

    def height(self, curnode):
        if curnode is None:
            return -1
        l_height = self.left.height(self.left)
        r_height = self.right.height(self.right)
        return max(l_height, r_height) + 1
