from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        n = len(nums)
        i, j = 0, 0
        k = 1
        prev = -1
        maxi = float("-inf")
        while j < n:

            if nums[j] == 0:
                if k == 0:
                    while i <= prev:
                        i += 1
                else:
                    k -= 1
                    prev = j + 1

            maxi = max(maxi, j - i + 1)
            j += 1

        return maxi


##### 2nd approach ########

from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        n = len(nums)
        i, j = -1, 0
        k = 1
        maxi = float("-inf")
        cnt = 0
        for j in range(n):

            if nums[j] == 0:
                cnt += 1

                while cnt > k:
                    i += 1
                    if nums[i] == 0:
                        cnt -= 1

            maxi = max(maxi, j - i)

        return maxi
