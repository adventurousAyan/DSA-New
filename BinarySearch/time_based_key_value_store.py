import collections

# https://leetcode.com/problems/time-based-key-value-store/


class TimeMap:
    def __init__(self):
        self.d1 = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d1[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        ls = self.d1[key]
        start = 0
        end = len(ls) - 1
        res = ""

        while start <= end:

            mid = start + (end - start) // 2
            val, tst = ls[mid]
            if timestamp == tst:
                return val
            elif timestamp > tst:
                res = val
                start = mid + 1
            else:
                end = mid - 1
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
