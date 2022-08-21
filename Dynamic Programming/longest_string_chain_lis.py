import functools
from typing import List

# https://leetcode.com/problems/longest-string-chain/

# Similar to LIS, but here instead of compararing array elements, we have to check words
# if the difference of prev and next word is 1, then we need to store the answer in dp


class Solution:
    def longestStrChain(self, words: List[str]) -> int:

        # Check if words differ by atmost 1 using a two pinter technique
        def is_pred(word1, word2):

            if len(word1) != len(word2) + 1:
                return False

            fp = 0
            sp = 0

            while fp < len(word1):
                if sp < len(word2) and word1[fp] == word2[sp]:
                    fp += 1
                    sp += 1
                else:
                    fp += 1

            if fp == len(word1) and sp == len(word2):
                return True
            return False

        # Comparator function for sorting words based on length
        def mycmp(w1, w2):
            if len(w1) < len(w2):
                return -1
            elif len(w1) > len(w2):
                return 1
            else:
                return 0

        n = len(words)
        words = sorted(words, key=functools.cmp_to_key(mycmp))
        # DP same as LIS Pattern
        dp = [1] * n
        maxi = 1
        for i in range(n):
            for j in range(i):
                if is_pred(words[i], words[j]) and 1 + dp[j] > dp[i]:
                    dp[i] = 1 + dp[j]
                    maxi = max(maxi, dp[i])

        return maxi
