from math import ceil, log2
from typing import List

# https://leetcode.com/problems/range-sum-query-mutable/


class NumArray:
    def __init__(self, nums: List[int]):

        n = len(nums)
        # Height of segment tree
        x = (int)(ceil(log2(n)))

        # Maximum size of segment tree
        max_size = 2 * (int)(2**x) - 1

        # Allocate memory
        self.seg = [0] * max_size
        self.constructSegmentTree(nums, 0, 0, len(nums) - 1)
        self.nums = nums

    def update(self, index: int, val: int) -> None:
        n = len(self.nums)
        self.point_update(0, n - 1, index, val, 0)

    def sumRange(self, left: int, right: int) -> int:

        n = len(self.nums)
        return self.solve_range(0, n - 1, left, right, 0)

    def constructSegmentTree(self, nums, idx, low, high):
        # Base Case
        if low == high:
            self.seg[idx] = nums[low]
            return
        mid = low + (high - low) // 2
        self.constructSegmentTree(nums, 2 * idx + 1, low, mid)
        self.constructSegmentTree(nums, 2 * idx + 2, mid + 1, high)
        self.seg[idx] = self.seg[2 * idx + 1] + self.seg[2 * idx + 2]

    def solve_range(self, low, high, l, r, idx):
        if high < l or low > r:
            return 0
        elif low >= l and high <= r:
            return self.seg[idx]
        else:
            mid = low + (high - low) // 2
            left = self.solve_range(low, mid, l, r, 2 * idx + 1)
            right = self.solve_range(mid + 1, high, l, r, 2 * idx + 2)
            return left + right

    def point_update(self, low, high, node, val, idx):
        if low == high:
            self.seg[idx] = val
        else:
            mid = low + (high - low) // 2

            if node >= low and node <= mid:
                self.point_update(low, mid, node, val, 2 * idx + 1)
            else:
                self.point_update(mid + 1, high, node, val, 2 * idx + 2)

            self.seg[idx] = self.seg[2 * idx + 1] + self.seg[2 * idx + 2]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
