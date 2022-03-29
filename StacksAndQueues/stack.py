class Stack:
    def __init__(self, capacity):
        self.arr = [None] * capacity
        self.top = -1

    def push(self, val):
        if self.top == len(self.arr) - 1:
            raise Exception("Stack Overflow")
        else:
            self.top += 1
            self.arr[self.top] = val

    def pop(self):
        if self.top == -1:
            raise Exception("No items in stack")
        else:
            val = self.arr[self.top]
            self.top -= 1
            return val

    def peek(self):
        if self.top == -1:
            raise Exception("No items in stack")
        else:
            return self.arr[self.top]


s = Stack(5)

s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
# s.push(6)

print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
# print(s.pop())
