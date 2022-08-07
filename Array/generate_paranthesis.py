from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        op = n
        cl = n
        ls = []
        s = "("

        return self.solve(op - 1, cl, ls, s)

    def solve(self, op, cl, ls, s):

        if op == 0 and cl == 0:
            ls.append(s)
        else:
            if op != 0:
                self.solve(op - 1, cl, ls, s + "(")
            if cl > op:
                self.solve(op, cl - 1, ls, s + ")")

        return ls
