from collections import deque

# https://leetcode.com/problems/race-car/


class Solution:
    def racecar(self, target: int) -> int:

        #         def f(s, position, speed):
        #             if position == target:
        #                 return 0

        #             accel, rev = 1e9, 1e9
        #             if (speed < 0 and position > target) or (position < target and speed > 0):
        #                 accel =  1 + f(s + "A", position+speed, speed*2)
        #             if position < target and speed < 0:
        #                  rev =  1 + f(s + "R", position, 1)
        #             if position > target and speed > 0:
        #                     rev =  1 + f(s + "R", position, -1)
        #             return min(accel, rev)

        visited = set()
        q = deque()
        q.append((0, 0, 1))
        while len(q) > 0:
            move, pos, speed = q.popleft()

            if pos == target:
                return move

            if (pos, speed) in visited:
                continue

            visited.add((pos, speed))

            # Accelerate
            q.append((move + 1, pos + speed, speed * 2))
            # Reverse
            # Case 1 where pos + speed is less than target, but speed < 0, we need
            # to reverse to make it speed to 1
            if pos + speed < target and speed < 0:
                q.append((move + 1, pos, 1))
            # 2nd Case :- When pos +  speed is gretaer than target, and speed > 0
            # it means we overshot, so we need to reverse
            elif pos + speed > target and speed > 0:
                q.append((move + 1, pos, -1))
        return -1
