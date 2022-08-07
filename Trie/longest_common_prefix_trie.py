from typing import List

# https://leetcode.com/problems/longest-common-prefix/


class TrieNode:
    def __init__(self):
        self.children = {}
        self.wc = 0
        self.endOfWord = False

    def __repr__(self):
        return repr(self.children)


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        cur = TrieNode()
        n = len(strs)

        for str1 in strs:
            self.insert(str1, cur)
        # print(cur)

        return self.longest_prefix(cur)

    def insert(self, s, cur):
        for c in s:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def longest_prefix(self, cur):
        res = []
        while cur:
            # return when reaches the end of word or when there are more than 1 branches
            if cur.endOfWord or len(cur.children) > 1:
                return "".join(res)
            c = list(cur.children)[0]
            res.append(c)
            cur = cur.children[c]
        return "".join(res)
