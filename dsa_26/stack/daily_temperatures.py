class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = [0]*len(temperatures)
        st = []



        for idx, val in enumerate(temperatures):
            
            while st and st[-1][0] < val:
                item, idx1 = st.pop()
                res[idx1] = idx-idx1
            st.append((val, idx))
        return res