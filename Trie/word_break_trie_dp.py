class TrieNode:
    def __init__(self):
        self.children = {}
        self.terminal = False
        self.data = None


class Solution:

    # https://leetcode.com/problems/word-break/

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        self.root = TrieNode()

        for word in wordDict:
            self.insert(word)

        def f(s, i):
            if dp[i] != -1:
                return dp[i]
            if i == len(s):
                dp[i] == True
                return True
            s1 = ""
            for j in range(i, len(s)):
                s1 += s[j]
                if self.search(s1):
                    if f(s, j + 1):
                        dp[i] = True
                        return True
                    else:
                        continue
            dp[i] = False
            return False

        dp = [-1] * 301
        return f(s, 0)

    def insert(self, word: str) -> None:

        cur = self.root
        for ch in word:
            if not cur.children.get(ch):
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.terminal = True

    def search(self, word: str) -> bool:
        cur = self.root
        for ch in word:
            if not cur.children.get(ch):
                return False
            cur = cur.children[ch]
        return cur.terminal
