class Solution:

    # https://leetcode.com/problems/permutation-sequence/
    # https://www.youtube.com/watch?v=wT7gcXLYoao for intuition

    def getPermutation(self, n: int, k: int) -> str:

        nums = [n] * n

        fact = 1
        for i in range(1, n):
            fact *= i
            nums[i - 1] = i

        ans = ""
        k = k - 1
        while True:

            ans += str(nums[k // fact])
            nums.remove(nums[k // fact])
            if len(nums) == 0:
                break

            k = k % fact

            fact = fact // len(nums)
        return ans


# TC: O(N2), SC: O(N)
