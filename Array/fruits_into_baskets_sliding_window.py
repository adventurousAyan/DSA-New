from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        i, j = 0, 0
        d1 = {}
        maxi = 1
        cnt = 0
        k = 2

        n = len(fruits)

        while j < n:

            val = fruits[j]

            if d1.get(val, 0) == 0:
                cnt += 1
            d1[val] = d1.get(val, 0) + 1
            if cnt > k:
                while cnt > k:
                    d1[fruits[i]] -= 1
                    if d1[fruits[i]] == 0:
                        cnt -= 1
                    i += 1

            maxi = max(maxi, j - i + 1)
            j += 1
        return maxi
