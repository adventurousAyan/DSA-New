from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        d1 = {}

        for val in strs:
            key = "".join(sorted(val))
            if key not in d1:
                d1[key] = [val]
            else:
                d1[key] += [val]

        return d1.values()
