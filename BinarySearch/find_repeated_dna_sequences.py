import collections
from typing import List


class Solution:

    # https://leetcode.com/problems/repeated-dna-sequences/

    def findRepeatedDnaSequences(self, s: str) -> List[str]:

        n = len(s)
        i, j = 0, 0
        d1 = {}
        q = collections.deque()
        ls = []
        while j < n:
            q.append(s[j])
            if j - i + 1 < 10:
                j += 1
            elif j - i + 1 == 10:
                s1 = "".join(q)
                d1[s1] = d1.get(s1, 0) + 1
                if d1[s1] > 1 and s1 not in ls:
                    ls.append(s1)
                q.popleft()
                i += 1
                j += 1
        return ls
