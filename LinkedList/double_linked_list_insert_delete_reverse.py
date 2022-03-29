class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.rear = None
        self.item_count = 0

    def insert(self, data):
        if self.head is None:
            self.head = Node(data)
            self.rear = self.head
            self.item_count = self.item_count + 1
            return self.head
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = Node(data)
            cur.next.prev = cur
            self.rear = cur.next
            self.item_count = self.item_count + 1
            return cur.next

    def print_elements(self):
        if self.head is None:
            raise ("DLL is empty")
        else:
            cur = self.head
            while cur:
                print(cur.data, end="")
                cur = cur.next

    def delete(self, data):
        if self.head is None:
            raise ("DLL is empty")
        elif data == self.head.data:
            self.head = self.head.next
        else:
            cur = self.head
            while cur:
                if cur.data == data:
                    break
                cur = cur.next

            if cur is not None:
                prev = cur.prev
                next = cur.next
                if prev:
                    prev.next = next
                if next:
                    next.prev = prev
            else:
                raise ("Element not found")

    def reverse(self):
        if self.head is None:
            raise ("DLL is empty")
        else:
            n = 0
            cur = self.head
            while cur.next:
                n = n + 1
                cur = cur.next
            rear = cur
            head = self.head
            lp = 0
            rp = n
            while lp <= rp and head.next and rear.prev:
                head.data, rear.data = rear.data, head.data
                head = head.next
                rear = rear.prev
                lp = lp + 1
                rp = rp - 1


# dll = DoubleLinkedList()

# dll.insert(6)
# dll.insert(7)
# dll.insert(1)
# dll.insert(4)
# dll.insert(5)
# dll.insert(3)


# dll.print_elements()
# print()
# dll.delete(4)

# dll.print_elements()
# print()

# dll.delete(3)
# dll.delete(5)
# dll.delete(1)

# dll.delete(6)
# dll.delete(7)
# dll.delete(5)
# dll.delete(1)
# dll.delete(3)

# dll.reverse()

# dll.print_elements()
