class MyCalendarTwo:
    # https://leetcode.com/problems/my-calendar-ii/
    # You tube video of line sweep algo with boundary count
    # https://www.youtube.com/watch?v=ElJdCIhkkZ8

    def __init__(self):
        self.d1 = {}

    def book(self, start: int, end: int) -> bool:
        self.d1[start] = self.d1.get(start, 0) + 1
        self.d1[end] = self.d1.get(end, 0) - 1
        self.d1 = dict(sorted(self.d1.items(), key=lambda kv: kv[0]))

        cnt = 0
        for k, val in self.d1.items():
            cnt += val
            if cnt > 2:
                self.d1[start] = self.d1.get(start, 0) - 1
                self.d1[end] = self.d1.get(end, 0) + 1
                return False
        return True
