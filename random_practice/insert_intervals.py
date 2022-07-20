from typing import List

# https://leetcode.com/problems/insert-interval/


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:

        ls = []
        flag = -1
        for intrvl in intervals:
            if newInterval[1] < intrvl[0]:
                ls.append(newInterval)
                newInterval = intrvl
                flag = 0
            elif intrvl[1] < newInterval[0]:
                ls.append(intrvl)
                flag = 1
            else:
                minno = min(newInterval[0], intrvl[0])
                maxno = max(newInterval[1], intrvl[1])
                newInterval = [minno, maxno]
        ls.append(intrvl) if flag == 0 else ls.append(newInterval)
        return ls
