from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def f(i, j):

            # Base Case:
            if i == 0:
                return points[i][j]
            maxi = float("-inf")
            for k in range(n - 1, -1, -1):

                res = points[i][k] + f(i - 1, k) - abs(j - k)
                print((i, k))
                print(f"Res:{res}")
                if res > maxi:
                    maxi = res
                print(f"Res:{res}")

            return maxi

        m = len(points)
        n = len(points[0])

        return f(m - 1, n - 1)
