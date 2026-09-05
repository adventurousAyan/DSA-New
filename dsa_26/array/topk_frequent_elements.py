class Solution:
    # https://leetcode.com/problems/top-k-frequent-elements/

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        d1 = {}
        # Put the elements in a dictionary with their frequency
        for num in nums:
            d1[num] = d1.get(num, 0) + 1

        # Sort the dictionary by frequency in descending order
        d2 = dict(sorted(d1.items(), key=lambda x: x[1], reverse=True))
        ls = []
        # Append the elements to the list until k is reached
        for key, v in d2.items():
            ls.append(key)
            k-= 1
            if k == 0:
                break
        return ls

# Above in unoptimized which still got accepted. We can optimize further by using heap
#TC: O(n log n)
#SC: O(n)