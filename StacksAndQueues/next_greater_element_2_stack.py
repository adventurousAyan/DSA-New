from typing import List


class Solution:
    # https://leetcode.com/problems/next-greater-element-ii/
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        stack = []
        new_list = [-1] * len(nums)
        n = len(nums)
        for i in range((2 * n) - 1, -1, -1):
            circular_idx = i % n
            while len(stack) > 0 and stack[-1] <= nums[circular_idx]:
                stack.pop()
            if len(stack) > 0 and  stack[-1] > nums[circular_idx] :
                new_list[circular_idx] = stack[-1]
            stack.append(nums[circular_idx])

        return new_list
