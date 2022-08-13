from typing import List


class Solution:
    # https://leetcode.com/problems/majority-element/
    # [2,2,1,1,1,2,2]
    # We will assume the first element as majority element and traverse the array. If we found the element , increase count , else decrease count
    # If count becomes 0 and the current element is not equal to the assumed majority element, we discard the majority and assign the current value as the majority and
    # move forward. This is based on Bayer Moore's Algorithm

    def majorityElement(self, nums: List[int]) -> int:

        count = 1
        res = nums[0]

        for i in range(1, len(nums)):
            if res == nums[i]:
                count += 1
            else:
                count -= 1

            if count == 0 and nums[i] != res:
                res = nums[i]
                count = 1
        return res
