from double_linked_list_insert_delete_reverse import (
    DoubleLinkedList,
    Node,
)


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dll = DoubleLinkedList()
        self.d1 = {}

    def put(self, data):
        if self.d1.get(data, "") == "":
            if self.dll.item_count != self.capacity:
                node = self.dll.insert(data)
                self.d1[data] = node
            else:
                oldhead = self.dll.head
                newnode = Node(data)
                oldrear = self.dll.rear
                self.dll.rear = newnode
                oldrear.next = self.dll.rear
                self.dll.rear.prev = oldrear
                self.d1[self.dll.rear.data] = self.dll.rear
                self.dll.head = oldhead.next
                self.d1[oldhead.data] = ""

        else:
            node = self.d1.get(data)
            prev = node.prev
            next = node.next
            if prev and next:
                prev.next = next
                next.prev = prev
            elif next:
                self.head = next
            elif prev:
                pass
            newnode = Node(data)
            oldrear = self.dll.rear
            self.dll.rear = newnode
            oldrear.next = self.dll.rear
            self.dll.rear.prev = oldrear
            self.d1[self.dll.rear.data] = self.dll.rear

    def print_items(self):
        self.dll.print_elements()


cache = LRUCache(4)
cache.put(3)
cache.put(1)
cache.put(5)
cache.put(6)
cache.put(7)
cache.put(5)
cache.put(6)
cache.put(8)

cache.print_items()
