class Queue1:
    def __init__(self, capacity):
        self.arr = [None] * capacity
        self.front = -1
        self.rear = -1

    def enqueue(self, val):
        if self.rear == len(self.arr) - 1:
            raise Exception("Queue is full")
        else:
            self.rear += 1
            self.arr[self.rear] = val

    def dequeue(self):
        if self.front == len(self.arr) - 1:
            raise Exception("No items in queue")
        else:
            self.front += 1
            val = self.arr[self.front]
            return val

    def empty(self):
        return self.front == len(self.arr) - 1


s = Queue1(5)

s.enqueue(1)
s.enqueue(2)
s.enqueue(3)
s.enqueue(4)
s.enqueue(5)
# s.enqueue(6)

print(s.dequeue())
print(s.dequeue())
print(s.dequeue())
print(s.dequeue())
print(s.dequeue())
# print(s.dequeue())
