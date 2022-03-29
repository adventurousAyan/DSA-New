class Solution:

    # Function to find the maximum number of meetings that can
    # be performed in a meeting room.
    def maximumMeetings(self, n, start, end):
        # code here

        ls = []
        n = len(start)
        for i in range(len(start)):
            ls.append((end[i], start[i]))
        ls = sorted(ls)
        start = []
        end = []
        for i in range(n):
            start.append(ls[i][1])
            end.append(ls[i][0])
        prev = 0
        cnt = 0
        for i in range(n):
            if end[i] > start[i] and start[i] > prev:
                cnt += 1
                prev = end[i]
        return cnt
