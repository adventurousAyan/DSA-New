class MinStack:

    def __init__(self):
        self.st = []
        

    def push(self, value: int) -> None:
        if len(self.st) == 0:
            self.st.append((value, value))
        else:
            if value < self.st[-1][1]:
                self.st.append((value, value))
            else:
                self.st.append((value, self.st[-1][1]))
       

    def pop(self) -> None:
            self.st.pop()
        

    def top(self) -> int:
        return self.st[-1][0]
        

    def getMin(self) -> int:
        return self.st[-1][1]

# Hint: Use a stack to store the elements and a variable to 
# store the minimum element seen so far.
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()