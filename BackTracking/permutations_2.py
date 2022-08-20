class Solution:

    # https://leetcode.com/problems/permutations-ii/

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def swap(nums, i, j):
            nums[i], nums[j] = nums[j], nums[i]

        def f(nums, idx, ls):

            if idx == len(nums):
                if nums.copy() not in self.l1:
                    self.l1.append(nums.copy())
                return

            for i in range(idx, len(nums)):

                if i + 1 < len(nums) and nums[i] == nums[i + 1]:
                    continue
                swap(nums, i, idx)
                f(nums, idx + 1, ls)
                swap(nums, i, idx)

        self.l1 = []
        nums = sorted(nums)
        f(nums, 0, [])
        return self.l1
