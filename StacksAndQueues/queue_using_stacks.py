class MyQueue:

    # https://leetcode.com/problems/implement-queue-using-stacks/submissions/

    def __init__(self):
        
        self.arr1 = []
        self.arr2 = []
        

    def push(self, x: int) -> None:
        while len(self.arr1) != 0:
            val = self.arr1.pop()
            self.arr2.append(val)
        self.arr1.append(x)
        while len(self.arr2) != 0:
            val = self.arr2.pop()
            self.arr1.append(val)
        

    def pop(self) -> int:
        return self.arr1.pop()
        

    def peek(self) -> int:
        return self.arr1[len(self.arr1)-1]
        

    def empty(self) -> bool:
        return len(self.arr1) == 0
        
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()