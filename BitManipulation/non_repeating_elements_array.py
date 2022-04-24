class Solution:
    # https://practice.geeksforgeeks.org/problems/finding-the-numbers0215/1

    def singleNumber(self, nums):
        # Code here

        xor = 0
        x = 0
        y = 0

        for num in nums:
            xor = xor ^ num

        right_most_set_bit = xor & ~(xor - 1)

        for i in range(len(nums)):
            if right_most_set_bit & nums[i] > 0:
                x = x ^ nums[i]
            else:
                y = y ^ nums[i]

        ls = []
        if x < y:
            ls.append(x)
            ls.append(y)
        else:
            ls.append(y)
            ls.append(x)

        return ls
