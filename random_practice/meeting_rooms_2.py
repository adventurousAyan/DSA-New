from queue import PriorityQueue

# https://leetcode.com/problems/meeting-rooms-ii/

from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        intervals = sorted(intervals, key=lambda x: x[0])

        conf_rooms = 1
        q = PriorityQueue()
        q.put(intervals[0][1])
        for i in range(1, len(intervals)):
            val = q.get()
            if intervals[i][0] < val:
                conf_rooms += 1
                q.put(val)
            q.put(intervals[i][1])

        return conf_rooms
