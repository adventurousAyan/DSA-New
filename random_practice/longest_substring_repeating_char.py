class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # https://leetcode.com/problems/longest-substring-without-repeating-characters/

        unique_dict = {}
        s = list(s)
        n = len(s)
        maxi = 0
        lp = 0
        rp = 0

        while lp <= rp and rp < n:

            if unique_dict.get(s[rp], 0) == 0:
                unique_dict[s[rp]] = 1
                maxi = max(maxi, rp - lp + 1)
                rp += 1
            else:
                unique_dict[s[lp]] -= 1
                lp += 1

        return maxi
