from collections import defaultdict, deque
from typing import List


class Solution:
    def findLadders(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> List[List[str]]:

        d1 = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                w1 = word[:i] + "*" + word[i + 1 :]
                d1[w1].append(word)

        q = deque()
        # print(d1)
        q.append((beginWord, [beginWord]))
        visited = set()
        ls = []
        while len(q) > 0:
            cur_layer = set()
            for _ in range(len(q)):
                word, path = q.popleft()
                if word == endWord:
                    ls.append(path)

                for i in range(len(beginWord)):
                    nextword = word[:i] + "*" + word[i + 1 :]
                    for nei in d1[nextword]:
                        if nei not in visited:
                            q.append((nei, path + [nei]))
                            cur_layer.add(nei)
            visited = visited.union(cur_layer)

        return ls
