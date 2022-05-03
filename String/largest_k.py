from typing import List

# https://algo.monster/problems/largest_k_positive_and_negative


def largest_k(nums: List[int]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    d1 = {}
    maxno = 0
    for a in nums:
        d1[a] = d1.get(a, 0) + 1

    for a in nums:
        if d1.get(a, -1) != -1 and d1.get(-a, -1) != -1:
            maxno = max(a, maxno)
    return maxno
