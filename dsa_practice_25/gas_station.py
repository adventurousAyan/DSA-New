class Solution:
    # TLE Solution
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        n = len(gas)
        gas1 = gas + gas
        cost1 = cost + cost

        for idx in range(n):
            cap = gas1[idx]
            for j in range(idx + 1, idx + n + 1):
                cap = cap - cost1[j-1] + gas1[j]
                if  cap < gas1[j]:
                    break
                if j > idx and idx == j%n:
                    return idx
        return -1