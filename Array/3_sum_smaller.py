class Solution:

    # https://leetcode.com/problems/3sum-smaller/submissions/
    def threeSumSmaller(self, nums: List[int], target: int) -> int:

        nums = sorted(nums)
        n = len(nums)
        cnt = 0

        for i in range(n - 1):
            lp = i + 1
            rp = n - 1
            while lp < rp:
                ss = nums[i] + nums[lp] + nums[rp]

                if ss < target:
                    # Here doing cnt += rp-lp as if we found a sum less than target, as array is sorted
                    # by moving the right pointer, we will get shortest sum as well
                    cnt += rp - lp
                    lp += 1
                else:
                    rp -= 1

        return cnt
