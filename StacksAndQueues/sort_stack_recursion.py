class Solution:
    # your task is to complete this function
    # function sort the stack such that top element is max
    # funciton should return nothing
    # s is a stack
    def sorted(self, s):
        # Code here
        if len(s) == 0:
            return
        val = s.pop()
        self.sorted(s)
        self.insert(s, val)
        return s

    def insert(self, s, val):

        if len(s) == 0 or val > s[len(s) - 1]:
            s.append(val)
        else:
            v = s.pop()
            self.insert(s, val)
            s.append(v)
