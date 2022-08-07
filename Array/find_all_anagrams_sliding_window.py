from typing import List


class Solution:

    # https://leetcode.com/problems/find-all-anagrams-in-a-string/

    def findAnagrams(self, s: str, p: str) -> List[int]:

        n = len(s)
        i, j = 0, 0
        ls = []
        k = len(p)

        d1 = {}

        for val in p:
            d1[val] = d1.get(val, 0) + 1

        counter = len(d1)

        while j < n:

            if s[j] in d1:
                d1[s[j]] -= 1
                if d1[s[j]] == 0:
                    counter -= 1

            if j - i + 1 < k:
                j += 1
            else:
                if counter == 0:
                    ls.append(i)
                if s[i] in d1:
                    d1[s[i]] += 1
                    if d1[s[i]] == 1:
                        counter += 1
                i += 1
                j += 1
        return ls
