
# https://leetcode.com/problems/min-stack/
class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = float('inf')
        

    def push(self, val: int) -> None:
        
        if len(self.stack) == 0:
            self.mini = val
            self.stack.append(val)
        elif val >= self.mini:
            self.stack.append(val)
        else:
            # If val is less than minimum element, encrypt the value using 2*val-min_element and store it. Mini element will be set to val
            self.stack.append(2*val-self.mini)
            self.mini = val
        

    def pop(self) -> None:
        
        # If value is less than minimum element, to get the earlier minimum element, we have to do 2*min_element-stack top
        if self.stack[-1] < self.mini:
            self.mini = 2*self.mini-self.stack[-1]
            
        self.stack.pop()
            
            
        

    def top(self) -> int:
        # If value is less than minimum element, then return minimum 
        if self.stack[-1] < self.mini:
            return self.mini
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.mini