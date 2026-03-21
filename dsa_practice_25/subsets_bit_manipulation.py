class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

      """
      https://leetcode.com/problems/subsets/?envType=problem-list-v2&envId=bit-manipulation
      
      Intuition:
      Let’s consider [1, 2, 3].
      
      If we get the binary representation for 0–7 (which is the number of subsets), it becomes:
      000, 001, 010, 011, 100, 101, 110, 111
      
      Now the problem reduces to finding the indexes of the set bits, which denote the subsets.
      
      For example:
      For 011 (i.e., 3), the set bits correspond to [2, 3].
    """

        n = len(nums)
        no_of_subsets = 1 << n
        res = []
        for i in range(no_of_subsets):
            ls = []
            for j in range(n):
                if ((1 << j) & i) != 0:
                    ls.append(nums[n-j-1])
            res.append(ls)
        return res
