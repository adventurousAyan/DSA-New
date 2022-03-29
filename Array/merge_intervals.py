from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda x: x[0])
        i = 0
        
        while i < len(intervals):
            
            if i == len(intervals)-1:
                break
            
            if intervals[i][1] >= intervals[i+1][0]:
                minno = min(intervals[i][0], intervals[i+1][0])
                maxno = max(intervals[i][1], intervals[i+1][1])
                intervals[i] = 0
                intervals[i+1] = [minno, maxno]
            i = i + 1
        
        ls = [x for x in intervals if x!= 0]
        
        return ls