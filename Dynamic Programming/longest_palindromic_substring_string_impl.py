class Solution:
    def longestPalindrome(self, s: str) -> str:

        str1 = ""
        max = float("-inf")
        for i in range(len(s)):
            l = i
            r = i
            # Odd Length
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    ln = r - l + 1
                    if ln > max:
                        max = ln
                        str1 = s[l : r + 1]
                else:
                    break
                l = l - 1
                r = r + 1

            # Even Length
            l = i
            r = i + 1
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    ln = r - l + 1
                    if ln > max:
                        max = ln
                        str1 = s[l : r + 1]
                else:
                    break
                l = l - 1
                r = r + 1

        return str1
