from typing import List

# https://leetcode.com/problems/minimum-time-difference/


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:

        n = len(timePoints)

        for i in range(n):
            val = timePoints[i].split(":")
            hrs = int(val[0])
            mins = int(val[1])
            if hrs == 0:
                hrs = 24
            timePoints[i] = hrs * 60 + mins

        timePoints = sorted(timePoints)
        print(timePoints)

        mini = float("inf")

        for i in range(n - 1):
            mini = min(mini, (timePoints[i + 1] - timePoints[i]))
        mini = min(1440 - (timePoints[-1] - timePoints[0]), mini)
        return mini
