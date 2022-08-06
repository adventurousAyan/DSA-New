from typing import List


class Solution:
    # https://leetcode.com/problems/divide-chocolate/

    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        def check_feasible(capacity, k):
            su = 0
            no_of_arrays = 0
            for num in sweetness:
                if su + num < capacity:
                    su += num
                else:
                    no_of_arrays += 1
                    su = 0

            return no_of_arrays >= k

        start = min(sweetness)
        end = sum(sweetness)
        while start <= end:

            mid = (start + end) // 2

            if check_feasible(mid, k + 1):
                start = mid + 1
            else:
                end = mid - 1

        return end
