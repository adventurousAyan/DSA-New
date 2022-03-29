from queue import Queue


class StackUsingQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.q1 = Queue(maxsize=capacity)
        self.q2 = Queue(maxsize=capacity)

    def push(self, data):
        if self.q1.full():
            raise ("Stack is Full")
        else:
            # self.q1.put(data)
            self.q2.put(data)
            while not self.q1.empty():
                self.q2.put(self.q1.get())

            while not self.q2.empty():
                self.q1.put(self.q2.get())

    def pop(self):
        if self.q1.empty():
            raise ("Stack is empty")
        else:
            return self.q1.get()


skq = StackUsingQueue(4)
skq.push(1)
skq.push(2)
skq.push(3)
skq.push(4)

print(skq.pop())
print(skq.pop())
print(skq.pop())
print(skq.pop())
