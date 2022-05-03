class Solution:
    # https://algo.monster/problems/longest_substring_without_3_contiguous_occurrences_letter
    def longestSubstring(self, s: str) -> int:

        lp = 0
        rp = 0
        a_count = 0
        b_count = 0
        maxno = float("-inf")

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
        return ans

    # Can we called but would involve extra swap
    def checkConsecutive(self, s1):
        a_count = 0
        b_count = 0
        for i in range(len(s1)):
            if s1[i] == "a":
                a_count += 1
                b_count = 0
            if s1[i] == "b":
                b_count += 1
                a_count = 0
            if a_count == 3 or b_count == 3:
                return False
        return True


s = Solution()
print(s.longestSubstring("aabbaaaaabb"))
