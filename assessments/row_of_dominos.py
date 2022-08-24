class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:

        d1 = defaultdict(int)
        n = len(tops)
        ls = set()
        for val1, val2 in zip(tops, bottoms):
            d1[val1] += 1
            d1[val2] += 1
            if d1[val1] >= n:
                ls.add(val1)
            if d1[val2] >= n:
                ls.add(val2)

        cnt1 = 0
        mini = float("inf")
        for val in ls:
            cnt1, cnt2 = 0, 0
            for i in range(n):
                if tops[i] != val and bottoms[i] != val:
                    return -1
                if tops[i] != val and bottoms[i] == val:
                    cnt1 += 1
                if bottoms[i] != val and tops[i] == val:
                    cnt2 += 1
            mini = min(mini, cnt1, cnt2)

        return mini if mini != float("inf") else -1
