from typing import List


class Solution:
    # https://leetcode.com/problems/best-sightseeing-pair/
    # We have to find pair such that values[i] + values[j] + i-j is maximum
    # We can also write this as (values[i] + i) + (values[j]-j)
    # We have to maximise (values[i] + i) + (values[j]-j)
    # https://www.youtube.com/watch?v=LeXxsRtxPY0
    def maxScoreSightseeingPair(self, values: List[int]) -> int:

        cur = values[0]
        ans = float("-inf")
        for j in range(1, len(values)):
            ans = max(ans, cur + values[j] - j)
            cur = max(cur, values[j] + j)
        return ans
