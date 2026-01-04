class Solution:
    def singleNumber(self, nums: List[int]) -> int:
      # Intuition - https://www.youtube.com/watch?v=5Bb2nqA40JY&t=283s
      # https://leetcode.com/problems/single-number-ii/description/?envType=problem-list-v2&envId=bit-manipulation
            res = 0
            for j in range(32):
                cnt = 0
                for n in nums:
                    if (1 << j) & n != 0:
                        cnt +=1
                if cnt%3 != 0:
                    res ^= 1 << j
            if res >= 1 << 31:
                res -= 1 << 32
            return res
        
