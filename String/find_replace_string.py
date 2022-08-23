from typing import List

# https://leetcode.com/problems/find-and-replace-in-string/


class Solution:
    def findReplaceString(
        self, s: str, indices: List[int], sources: List[str], targets: List[str]
    ) -> str:

        s1 = s
        ls = []

        ## Sort the indices by reverse order as we want to replace from back , so that indexing doesnt change
        for i in range(len(indices)):
            ls.append((indices[i], sources[i], targets[i]))

        ls = sorted(ls, key=lambda x: x[0], reverse=True)
        indices, sources, targets = [], [], []
        for idx, source, target in ls:
            indices.append(idx)
            sources.append(source)
            targets.append(target)

        # Check if substring sub is contained in s
        def check_sub(pos, sub):

            fp = 0
            sp = pos
            while fp < len(sub) and sp < len(s):
                if sub[fp] == s1[sp]:
                    fp += 1
                    sp += 1
                else:
                    return False

            if fp == len(sub):
                return True

        n = len(indices)

        def dfs(i, s):

            if s == "":
                return ""
            if i == n:
                return s

            pos = indices[i]
            source = sources[i]
            target = targets[i]
            # If the string exists at that particular index, then perform the replace of string from the target
            if check_sub(pos, source):
                s = s[:pos] + target + s[pos + len(source) :]
            # Do dfs
            return dfs(i + 1, s)

        return dfs(0, s)
