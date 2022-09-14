# There is a set of n items. You are given two integer arrays values and labels where the value and the label of the ith element are values[i] and labels[i] respectively. You are also given two integers numWanted and useLimit.

# Choose a subset s of the n elements such that:

# The size of the subset s is less than or equal to numWanted.
# There are at most useLimit items with the same label in s.
# The score of a subset is the sum of the values in the subset.

# Return the maximum score of a subset s.

# Input: values = [5,4,3,2,1], labels = [1,1,2,2,3], numWanted = 3, useLimit = 1
# Output: 9
# Explanation: The subset chosen is the first, third, and fifth items.


from collections import defaultdict
from typing import List


class Solution:
    def largestValsFromLabels(
        self, values: List[int], labels: List[int], numWanted: int, useLimit: int
    ) -> int:

        n = len(values)

        ls = []
        for i in range(n):
            ls.append((values[i], labels[i]))

        ls = sorted(ls, key=lambda x: x[0], reverse=True)
        su = 0
        d1 = defaultdict(int)
        no = 1
        for val, lbl in ls:
            d1[lbl] += 1
            if d1[lbl] <= useLimit and no <= numWanted:
                no += 1
                su += val
        return su
