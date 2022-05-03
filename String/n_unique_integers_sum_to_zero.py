from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        k = n // 2

        s = 0
        ls = []
        for i in range(-k, k + 1):
            if n % 2 == 0:
                if i != 0:
                    s += i
                    ls.append(i)
                else:
                    pass
            else:
                s += i
                ls.append(i)

        return ls
