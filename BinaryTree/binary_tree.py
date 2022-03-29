import queue
from queue import Queue


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.left is None:
            self.left = Node(data)
        else:
            self.left.insert(data)
        if self.right is None:
            self.right = Node(data)
        else:
            self.right.insert(data)

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.data)
        if self.right:
            self.right.inorder()

    def height(self):
        if self.left:
            lheight = 1 + self.left.height()
        if self.right:
            rheight = 1 + self.right.height()
        else:
            return 1
        return max(lheight, rheight)


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.root.insert(data)

    def inorder(self):
        if self.root is None:
            print("Tree is empty")
        else:
            self.root.inorder()

    def height(self):
        if self.root is None:
            return 0
        else:
            return self.root.height()

    def level_order(self):
        if self.root is None:
            print("Tree is empty")
        else:
            q = Queue(20)
            q.put(self.root)
            while not q.empty():
                val = q.get()
                if val:
                    print(val.data)
                    if val.left:
                        q.put(val.left)
                    if val.right:
                        q.put(val.right)

    def top_bottom_view(self):
        d1 = {}
        if self.root is None:
            print("Tree is empty")
        else:
            q = Queue(20)
            levelq = Queue(20)
            q.put(self.root)
            levelq.put(0)
            llevel = 0
            rlevel = 0
            d1[0] = str(self.root.data)
            while not q.empty():
                val = q.get()
                level = levelq.get()
                if val.left:
                    llevel = level - 1
                    q.put(val.left)
                    levelq.put(llevel)
                    if d1.get(llevel):
                        d1[llevel] = d1.get(llevel) + "," + str(val.left.data)
                    else:
                        d1[llevel] = str(val.left.data)
                if val.right:
                    rlevel = level + 1
                    q.put(val.right)
                    levelq.put(rlevel)
                    if d1.get(rlevel):
                        d1[rlevel] = d1.get(rlevel) + "," + str(val.right.data)
                    else:
                        d1[rlevel] = str(val.right.data)
        d1 = sorted(d1.items(), key=lambda x: x[0])

        # Top View
        print("****TOP VIEW****")
        for val in d1:
            ls = val[1].split(",")
            print(ls[0], end=" ")

        print()
        # Bottom View
        print("****BOTTOM VIEW****")
        for val in d1:
            ls = val[1].split(",")
            n = len(ls)
            print(ls[n - 1], end=" ")


b = BinaryTree()
b.root = Node(3)
b.root.left = Node(7)
b.root.left.left = Node(9)
b.root.left.right = Node(1)
b.root.left.right.left = Node(2)
b.root.left.right.right = Node(3)
b.root.right = Node(6)
b.root.right.left = Node(10)
b.root.right.right = Node(15)


# b.inorder()

# print(b.height())

b.top_bottom_view()
