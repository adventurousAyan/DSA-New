from typing import List

# https://leetcode.com/problems/koko-eating-bananas/


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def checkBananaPerHrSpeed(mid):

            total_hours = 0
            for pile in piles:
                total_hours += pile // mid
                if pile % mid != 0:
                    total_hours += 1

            return total_hours

        start = 1
        end = sum(piles)

        while start <= end:

            mid = start + (end - start) // 2

            if mid > 0 and checkBananaPerHrSpeed(mid) <= h:
                end = mid - 1
            else:
                start = mid + 1
        return start
