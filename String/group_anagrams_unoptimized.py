from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        strs = sorted(strs)
        n = len(strs)
        res = []
        for i in range(len(strs)):
            lp = i
            rp = i + 1
            if strs[lp] != "xxxx":
                ls = []
                ls.append(strs[lp])
                while lp < rp and rp < n:
                    w1 = strs[lp]
                    w2 = strs[rp]
                    if self.checkAnagram(w1, w2):
                        ls.append(strs[rp])
                        strs[rp] = "xxxx"
                    rp += 1

                res.append(ls)
        return res

    def checkAnagram(self, w1, w2):

        d1 = {}
        d2 = {}

        for a in w1:
            d1[a] = d1.get(a, 0) + 1

        for a in w2:
            d2[a] = d2.get(a, 0) + 1

        if d1 == d2:
            return True

        return False
