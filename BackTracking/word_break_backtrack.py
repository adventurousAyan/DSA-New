from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        if s == "":
            return True
        else:
            for word in wordDict:
                if word in s:
                    strtIndex, endIndex = self.findWordIndex(s, word)
                    # print(strtIndex)
                    if strtIndex == 0:
                        s = self.partitionWord(strtIndex, endIndex, word, s)
                        # print(s)
                        res = self.wordBreak(s, wordDict)
                        if res:
                            return True
                        else:
                            # print("Backtrack")
                            s = self.addWord(strtIndex, word, s)
                            # print(s)
            return False

    def findWordIndex(self, s, word):
        n = len(word)
        lp = 0
        rp = n - 1

        while lp <= rp and rp < len(s):
            s1 = s[lp : rp + 1]
            if s1 == word:
                return lp, rp
            else:
                lp = lp + 1
                rp = rp + 1
        return -1

    def partitionWord(self, strtIndex, endIndex, word, s):
        n = len(word)
        s2 = ""
        if strtIndex == 0:
            s2 = s[strtIndex + n :]
        else:
            for i in range(len(s)):
                if not (i >= strtIndex and i <= endIndex):
                    s2 = s2 + s[i]
        return s2

    def addWord(self, wordIndex, word, s):
        n = len(word)
        s2 = ""
        if wordIndex == 0:
            s2 = word + s
        else:
            for i in range(len(s)):
                if i == wordIndex:
                    s2 += word
                s2 += s[i]
        return s2
