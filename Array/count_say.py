class Solution:

    # https://leetcode.com/problems/count-and-say/

    def countAndSay(self, n: int) -> str:

        val = "1"
        for _ in range(2, n + 1):
            val = self.say_conversion(str(val))
        return val

    def say_conversion(self, val):
        val = list(val)
        lp, rp = 0, 0
        cnt = 0
        s = ""
        while lp <= rp and rp < len(val):

            if val[lp] == val[rp]:
                cnt += 1
                rp += 1
            else:
                s += f"{cnt}{val[lp]}"
                lp = rp
                cnt = 0
        s += f"{cnt}{val[lp]}"
        return s
