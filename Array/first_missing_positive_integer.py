from typing import List


class Solution:

    # https://leetcode.com/problems/first-missing-positive/

    def firstMissingPositive(self, nums: List[int]) -> int:

        num = 1
        # Remove numbers less than equal to 0
        nums = [x for x in nums if x > 0]
        # Remove duplicates and convert to set
        nums = set(nums)
        # Now check if num is within the set. If not increment num and continue checking
        while num in nums:
            num += 1
        return num


#############2nd Approach#####################################

# https://www.youtube.com/watch?v=9SnkdYXNIzM


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        n = len(nums)
        count_of_one = 0
        for i in range(n):
            if nums[i] == 1:
                count_of_one = 1
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1

        if count_of_one == 0:
            return 1

        for i in range(n):
            correct_pos = abs(nums[i]) - 1
            if nums[correct_pos] > 0:
                nums[correct_pos] = -1 * nums[correct_pos]

        for i in range(n):
            if nums[i] > 0:
                return i + 1
        return n + 1
