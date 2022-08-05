class MyCalendar:

    # https://leetcode.com/problems/my-calendar-i/

    def __init__(self):
        self.intervals = []

    def book(self, start: int, end: int) -> bool:
        for prevStart, prevEnd in self.intervals:
            if start >= prevStart and start < prevEnd:
                return False
            elif start < prevStart and end > prevStart:
                return False
        self.intervals.append([start, end])
        return True
