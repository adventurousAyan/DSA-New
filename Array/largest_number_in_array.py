import functools
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        nums = [str(x) for x in nums]

        nums = sorted(nums, key=functools.cmp_to_key(compare_func))

        return str(int("".join(nums)))


def compare_func(x, y):
    if x + y > y + x:
        return -1
    elif x + y < y + x:
        return 1
    else:
        return 0
