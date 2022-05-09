from functools import cmp_to_key

# https://leetcode.com/discuss/interview-experience/1994403/Coinbase-or-IC-4-or-Bangalore-or-March-2022-or-Offer


class Solution:
    def access_logs(self, logs, k=0):

        logs1 = sorted(logs, key=cmp_to_key(self.compare))

        n = len(logs1)

        d1 = {}

        mintime = 0
        maxtime = k

        max = int(logs1[n - 1][0])
        mylist = []
        while mintime >= 0 and maxtime < max:
            for ls in logs1:
                ts = int(ls[0])
                if ts > mintime and ts < maxtime:
                    resource = ls[2]
                    d1[resource] = d1.get(resource, 1) + 1
            d2 = {k: v for v, k in sorted(d1.items(), key=lambda x: x[1], reverse=True)}
            val = list(d2.items())[0]

            mylist.append(val)
            mintime += k
            maxtime += k

        return mylist

    def compare(self, x, y):
        val1 = x[0]
        val2 = y[0]
        if val1 < val2:
            return -1
        else:
            return 1


s = Solution()

s.access_logs(
    [
        ["58523", "user_1", "resource_1"],
        ["62314", "user_2", "resource_2"],
        ["54001", "user_1", "resource_3"],
        ["200", "user_6", "resource_5"],
        ["215", "user_6", "resource_4"],
        ["54060", "user_2", "resource_3"],
        ["53760", "user_3", "resource_3"],
        ["58522", "user_22", "resource_1"],
        ["53651", "user_5", "resource_3"],
        ["2", "user_6", "resource_1"],
        ["100", "user_6", "resource_6"],
        ["400", "user_7", "resource_2"],
        ["100", "user_8", "resource_6"],
        ["54359", "user_1", "resource_3"],
    ],
    300,
)
