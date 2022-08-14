from typing import List

# https://leetcode.com/problems/russian-doll-envelopes/


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:

        # Sort the array by width and reverse sort by height
        # You can also sort by the area i.e height*width
        # Then apply LIS
        # Gives TLE using the DP O(n2) approach
        envelopes = sorted(envelopes, key=lambda x: (x[0], -x[1]))

        n = len(envelopes)

        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if (
                    envelopes[j][0] < envelopes[i][0]
                    and envelopes[j][1] < envelopes[i][1]
                ):
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)
