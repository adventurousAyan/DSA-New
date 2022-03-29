from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        op = n
        cl = n

        ip = "("
        op = op - 1
        ls = []
        self.solve(ip, op, cl, ls)
        return ls

    def solve(self, ip, op, cl, ls):

        if op == 0 and cl == 0:
            ls.append(ip)
        else:
            if op != 0:
                self.solve(ip + "(", op - 1, cl, ls)
            if cl > op:
                self.solve(ip + ")", op, cl - 1, ls)
