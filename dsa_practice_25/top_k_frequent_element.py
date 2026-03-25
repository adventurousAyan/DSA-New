from queue import PriorityQueue

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        d = {}

        for num in nums:
            d[num] = d.get(num, 0) + 1

        pq = PriorityQueue()
        for key, value in d.items():
            pq.put((-value, key))

        ls = []

        while k != 0:
            priority, item =  pq.get()
            ls.append(item)
            k -=1
        return ls


        