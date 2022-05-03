class Solution:
    # https://algo.monster/problems/min_swaps_to_make_palindrome
    def minimumSwap(self, s: str) -> int:

        lp = 0
        rp = len(s) - 1
        minswap = 0
        if not self.isValidPalindrome(s):
            return -1

        while lp <= rp:
            if s[lp] != s[rp]:
                tmp = rp
                while s[tmp] != s[lp] and tmp != lp:
                    tmp -= 1
                if tmp == lp:
                    minswap += 1
                    s = self.swap(s, lp, lp + 1)
                else:
                    minlp = tmp
                    minrp = tmp + 1
                    while minlp <= minrp and minrp <= rp:
                        s = self.swap(s, minlp, minrp)
                        minswap += 1
                        minlp += 1
                        minrp += 1

            lp += 1
            rp -= 1
        return minswap

    def swap(self, s, minlp, minrp):
        s = list(s)
        s[minlp], s[minrp] = s[minrp], s[minlp]
        return "".join(s)

    def isValidPalindrome(self, s):
        n = len(s)
        maxcnt = 0
        d1 = {}
        for i in range(n):
            d1[s[i]] = d1.get(s[i], 0) + 1

        for k, v in d1.items():
            if v == 1:
                maxcnt += 1
            if maxcnt > 1:
                return False
        return True


s = Solution()
print(s.minimumSwap("aabcb"))
