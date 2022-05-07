class Solution:

    # https://leetcode.com/problems/implement-strstr/

    def strStr(self, haystack: str, needle: str) -> int:

        lp = 0
        rp = 1
        n = len(needle)
        ls = [0] * n
        ls[0] = 0
        # Form the LPS array
        while lp <= rp and rp < n:
            if needle[lp] != needle[rp]:
                if lp == 0:
                    ls[rp] = 0
                    rp = rp + 1
                else:
                    lp = ls[lp - 1]

            else:
                ls[rp] = 1 + lp
                lp = lp + 1
                rp = rp + 1

        n1 = len(haystack)
        l1 = 0
        l2 = 0
        while l1 < n and l2 < n1:
            if needle[l1] == haystack[l2]:
                if l1 == n - 1:
                    # The last character matches, so we got our substring and then
                    # just return the index
                    return l2 - n + 1
                else:
                    l1 += 1
                    l2 += 1

            else:
                if l1 == 0:
                    l2 += 1
                else:
                    l1 = ls[l1 - 1]
        return -1
