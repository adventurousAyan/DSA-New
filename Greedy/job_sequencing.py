class Solution:

    # Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self, Jobs, n):

        # code here
        jobs = Jobs
        ls = []
        for a in jobs:
            ls.append((a.deadline, a.profit))
        ls = sorted(ls, key=lambda x: x[1], reverse=True)
        l2 = [x[0] for x in ls]
        max_no = sorted(l2)[len(l2) - 1]
        l1 = [None] * max_no
        cnt = 0
        sum = 0
        for i in range(len(ls)):
            idx = ls[i][0]
            for j in range(idx - 1, -1, -1):
                if l1[j] is None:
                    l1[j] = ls[i][1]
                    cnt += 1
                    break

        for a in l1:
            if a is not None:
                sum += a

        return cnt, sum
