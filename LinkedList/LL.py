class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LL:
    def __init__(self) -> None:
        self.head = None

    def insert(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            curnode = self.head
            while curnode.next != None:
                curnode = curnode.next
            curnode.next = Node(data)

    def display(self):
        if not self.head:
            print("Linked list is empty")
        else:
            curnode = self.head
            while curnode.next != None:
                print(curnode.data)
                curnode = curnode.next


ll = LL()
ll.insert(5)
ll.insert(10)
ll.insert(15)
ll.insert(20)

ll.display()
