"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

# https://leetcode.com/problems/employee-free-time/


class Solution:
    def employeeFreeTime(self, schedule: "[[Interval]]") -> "[Interval]":

        ls = []

        for schedl in schedule:
            for intrvl in schedl:
                ls.append((intrvl.start, "B"))
                ls.append((intrvl.end, "E"))

        ls = sorted(ls, key=lambda x: x[0])

        bal = 0
        prev = -1
        res = []
        for val in ls:
            if prev != -1 and bal == 0 and prev[0] != val[0]:
                res.append(Interval(prev[0], val[0]))
            time, time_type = val
            if time_type == "B":
                bal += 1
            if time_type == "E":
                bal -= 1
            prev = val

        # print(res)
        return res
