class Solution:
    def isPalindrome(self, S):
        # code here

        lp = 0
        rp = len(S) - 1

        while lp <= rp:
            if S[lp] == S[rp]:
                lp += 1
                rp -= 1
            else:
                return 0
        return 1
