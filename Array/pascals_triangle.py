from typing import List


class Solution:

    # https://leetcode.com/problems/pascals-triangle/

    def generate(self, numRows: int) -> List[List[int]]:
        def f(i):
            if i == numRows:
                return
            if i == 0:
                self.ls.append([1])
            elif i == 1:
                self.ls.append([1, 1])
            else:
                tmp = []
                tmp.append(1)
                idx = i - 1
                lp, rp = 0, 1

                while lp < rp and rp < len(self.ls[idx]):
                    s = self.ls[idx][lp] + self.ls[idx][rp]
                    tmp.append(s)
                    lp += 1
                    rp += 1
                tmp.append(1)
                self.ls.append(tmp)
            f(i + 1)

        self.ls = []
        f(0)
        return self.ls
