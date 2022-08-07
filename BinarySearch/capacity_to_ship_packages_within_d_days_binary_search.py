from typing import List

# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check_feasible(capacity, days):
            su = 0
            day = 0
            for weight in weights:
                if weight > capacity:
                    return False
                if su + weight <= capacity:
                    su += weight
                else:
                    day += 1
                    su = weight
            day += 1
            return True if day <= days else False

        start = 0
        end = sum(weights)

        while start <= end:

            mid = (start + end) // 2

            if check_feasible(mid, days):
                end = mid - 1
            else:
                start = mid + 1

        return start
