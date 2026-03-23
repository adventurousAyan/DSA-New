class Solution:
    # https://leetcode.com/problems/combination-sum/description/
    # Intuition: https://www.youtube.com/watch?v=GBKI9VSKdGg
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        def solve(idx, target, ls):
            if target == 0:
                res.append(ls.copy())
                return
            if idx >= len(candidates):
                return
            if target >= candidates[idx]:
                ls.append(candidates[idx])
                solve(idx, target - candidates[idx], ls)
                ls.pop()
            solve(idx + 1, target, ls)
                    

        solve(0, target, [])



        return res