from collections import defaultdict
from typing import List

# This is a problem that needs some understanding. Basically there are two ways to solve the problem.
# One way is for the new point, find a point in similar x corordinate. If we are able to find,
# in order to be it a square, it other two points would be x1-(y2-y1), y1 and x1-(y2-y1), y2
# We can find the count fo those , multiply and return the answer

# For intuition, we can follow the below :-

# https://leetcode.com/problems/detect-squares/discuss/1471958/C%2B%2BJavaPython-2-approaches-using-HashMap-with-Picture-Clean-and-Concise


class DetectSquares:

    # https://leetcode.com/problems/detect-squares/

    def __init__(self):
        self.d1 = defaultdict(int)
        self.d2 = defaultdict(list)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.d1[(x, y)] += 1
        self.d2[x].append(y)

    def count(self, point: List[int]) -> int:

        x1, y1 = point
        cnt = 0
        for y2 in self.d2[x1]:
            if y1 == y2:
                continue
            diff = abs(y2 - y1)

            x3, y3 = x1 - diff, y1
            x4, y4 = x1 - diff, y2

            cnt += self.d1[(x3, y3)] * self.d1[(x4, y4)]

            x3, y3 = x1 + diff, y1
            x4, y4 = x1 + diff, y2

            cnt += self.d1[(x3, y3)] * self.d1[(x4, y4)]

        return cnt
