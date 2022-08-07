from typing import List


class Solution:

    # https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

    def maxScore(self, cardPoints: List[int], k: int) -> int:

        n = len(cardPoints)
        su = sum(cardPoints)

        window = n - k

        if window == 0:
            return su

        i, j = 0, 0

        s = 0
        maxi = float("-inf")
        while j < n:

            s += cardPoints[j]

            if j - i + 1 < window:
                j += 1
            elif j - i + 1 == window:
                # print(s)
                maxi = max(maxi, su - s)
                s -= cardPoints[i]
                i += 1
                j += 1
        return maxi
