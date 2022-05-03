class Solution:

    # https://algo.monster/problems/longest_semi_alternating_substring

    def longestSubstringAlternating(self, s: str) -> int:

        lp = 0
        rp = 0
        a_count = 0
        b_count = 0
        maxno = float("-inf")
        ans = ""
        while lp <= rp and rp < len(s):
            if s[rp] == "a":
                a_count += 1
                b_count = 0
            if s[rp] == "b":
                b_count += 1
                a_count = 0
            if not (a_count == 3 or b_count == 3):
                rp = rp + 1
            else:
                ln = rp - lp + 1
                if ln > maxno:
                    maxno = ln
                    ans = s[lp:rp]
                lp = rp - 1
        return len(ans) if ans else len(s)


s = Solution()
print(s.longestSubstringAlternating("abaaaa"))
