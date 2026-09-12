class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        
        
        def bs(nums, target):
            lp, rp = 0, len(nums) - 1
            while lp <= rp:
                mid  = lp + (rp - lp) // 2

                if nums[mid] == target:
                    return True
                elif target > nums[mid]:
                    lp = mid + 1
                else:
                    rp = mid - 1
            return False
        
        m, n = len(matrix), len(matrix[0])

        lp, rp = 0, m - 1

        ans = -1
        while lp <= rp:
            mid = lp + (rp - lp) // 2
            if matrix[mid][0] == target:
                return True
            elif target > matrix[mid][0]:
                ans = mid
                lp = mid + 1
            else:
                rp = mid - 1
        
        if bs(matrix[ans], target):
            return True
        return False