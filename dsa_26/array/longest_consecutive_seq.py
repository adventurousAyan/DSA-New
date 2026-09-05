class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        d1 = {}

        lonc_seq = 1
        maxi = float('-inf')

        if len(nums) == 0:
            return 0

        for num in nums:
            d1[num] = d1.get(num, 0) + 1

        vis = set()
        for num in nums:
            # If the number is already visited, skip it
            if num in vis:
                continue
            # If the number is not visited, add it to the visited set
            vis.add(num)
            lonc_seq = 1
            # Here is means, there is a number after the current number
            #So there is a consecutive sequence after the current number
            if num+1 in d1.keys():
                val = num + 1
                while d1.get(val):
                    vis.add(val)
                    lonc_seq +=1
                    maxi = max(maxi, lonc_seq)
                    val+=1
            # This is also for skipping redundant processing. Imagine a test case [5,4,3,2,1]
            # For this, if we only check for num+1, we will process multiple times for same nummber
            elif num-1 in d1.keys():
                val = num - 1
                while d1.get(val):
                    vis.add(val)
                    lonc_seq +=1
                    maxi = max(maxi, lonc_seq)
                    val-=1
        return max(maxi, lonc_seq)





        