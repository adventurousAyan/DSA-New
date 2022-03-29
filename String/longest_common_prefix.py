from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        lp = 0
        rp = 1
        prefix = ""
        if len(strs) == 1:
            prefix = strs[0]
        while lp < rp and rp < len(strs):
            prefix = self.find_prefix(strs[lp], strs[rp])
            if prefix == "":
                break
            else:
                strs[rp] = prefix
            lp += 1
            rp += 1

        return prefix

    def find_prefix(self, str1, str2):
        prefix = ""
        n = min(len(str1), len(str2))
        str1 = list(str1)
        str2 = list(str2)
        for i in range(n):
            if str1[i] == str2[i]:
                prefix = prefix + str1[i]
            else:
                break
        return prefix
