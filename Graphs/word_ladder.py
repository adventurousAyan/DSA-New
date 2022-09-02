from collections import defaultdict, deque
from typing import List

# https://leetcode.com/problems/word-ladder/
# Have asked for shortest transformation sequence, i.e the shortest path. DFS will not work in such scenario


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList:
            return 0

        d1 = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                w1 = word[:i] + "*" + word[i + 1 :]
                d1[w1].append(word)

        q = deque()
        visited = set()
        q.append(beginWord)
        res = 1
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word in visited:
                    continue
                if word == endWord:
                    return res
                visited.add(word)
                for i in range(len(word)):
                    w1 = word[:i] + "*" + word[i + 1 :]
                    neibors = d1[w1]
                    for nei in neibors:
                        if nei not in visited:
                            q.append(nei)
            res += 1
        return 0
