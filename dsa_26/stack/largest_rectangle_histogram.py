class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:


        st = []
        st1 = []
        n = len(heights)
        res1 = [n]*len(heights)

        res2 = [n]*len(heights)

        for idx, ht in enumerate(heights):
            while st and heights[st[-1]] > ht:
                idx1 = st.pop()
                res1[idx1] = idx
            st.append(idx)
        
        heights1 = heights[::-1]
        for idx, ht in enumerate(heights1):
            while st1 and heights1[st1[-1]] > ht:
                idx1 = st1.pop()
                res2[idx1] = idx
            st1.append(idx)

        res3 = res2[::-1]

        maxi = float('-inf')
        for idx, ht in enumerate(heights):
            rec_len = 0
            if res1[idx] != -1:
                rec_len = res1[idx] - (n-res3[idx])
            else:
                rec_len = n - idx
            maxi = max(maxi, ht*rec_len)

        return maxi






        