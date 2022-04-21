import math


class Solution:

    # Function to delete middle element of a stack.
    def deleteMid(self, s, sizeOfStack):
        mid = int((sizeOfStack + 1) / 2) - 1
        self.delete_mid(s, mid)

    def delete_mid(self, s, mid):
        n = len(s)
        if n == 0:
            return s
        if n - 1 == mid:
            s.pop()
            return s
        else:
            val = s.pop()
            self.delete_mid(s, mid)
            s.append(val)
