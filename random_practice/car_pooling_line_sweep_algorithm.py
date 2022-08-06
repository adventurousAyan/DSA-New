from typing import List

# https://leetcode.com/problems/car-pooling/


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        ls = []

        for trip in trips:
            pasen = trip[0]
            ls.append((trip[1], "B", pasen))
            ls.append((trip[2], "E", pasen))

        ls = sorted(ls, key=lambda x: x[0])

        capa = 0
        trip = 0
        prev = -1
        for val in ls:
            time, journey_type, pasen = val
            if prev != -1 and capa > capacity and prev != time:
                return False
            if journey_type == "B":
                trip += 1
                capa += pasen

            if journey_type == "E":
                capa -= pasen
                trip -= 1
            prev = time

        return capa == 0 and trip == 0
