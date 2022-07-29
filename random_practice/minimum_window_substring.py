class Solution:

    # https://leetcode.com/problems/minimum-window-substring/

    # This approach gives TLE

    def minWindow(self, s: str, t: str) -> str:
        def check_str(s1):
            d1 = {}
            for ch in s1:
                d1[ch] = d1.get(ch, 0) + 1

            for ch in t:
                if d1.get(ch, 0) != 0:
                    d1[ch] -= 1
                else:
                    return False
            return True

        n1 = len(t)
        lp, rp, n = 0, n1 - 1, len(s)

        d1 = {}
        mini = float("inf")
        ans = ""

        if n1 > n:
            return ans
        while lp <= rp and rp < n:
            s1 = s[lp : rp + 1]
            res = check_str(s1)
            if res:
                ln = len(s1)
                if ln < mini:
                    mini = ln
                    ans = s1
                    print(ans)
                lp += 1
            else:
                rp += 1
        return ans


#######Second approach##########


def minWindow(self, s: str, t: str) -> str:
    def check_str(s1):
        d2 = d1.copy()
        for ch in t:
            if d2.get(ch, 0) != 0:
                d2[ch] -= 1
            else:
                return False
        return True

    n1 = len(t)
    lp, rp, n = 0, n1 - 1, len(s)

    d1 = {}
    mini = float("inf")
    ans = ""
    if n1 > n:
        return ans
    for i in range(0, n1):
        d1[s[i]] = d1.get(s[i], 0) + 1

    while lp <= rp and rp < n:
        s1 = s[lp : rp + 1]
        res = check_str(s1)
        if res:
            ln = len(s1)
            if ln < mini:
                mini = ln
                ans = s1
                # print(ans)
            d1[s[lp]] -= 1
            lp += 1

        else:
            rp += 1
            if rp < n:
                d1[s[rp]] = d1.get(s[rp], 0) + 1
    return ans


#######3rd approach##########


class Solution:

    # https://leetcode.com/problems/minimum-window-substring/

    # https://www.youtube.com/watch?v=jSto0O4AJbM

    class Solution:
        def minWindow(self, s: str, t: str) -> str:
            n1 = len(t)
            lp, rp, n = 0, 0, len(s)

            d1, d2 = {}, {}
            mini = float("inf")
            ans = ""
            if n1 > n:
                return ans

            for i in range(0, n1):
                d1[t[i]] = d1.get(t[i], 0) + 1

            have, need = 0, len(d1)
            while lp <= rp and rp < n:
                d2[s[rp]] = d2.get(s[rp], 0) + 1
                if s[rp] in d1 and d2[s[rp]] == d1[s[rp]]:
                    have += 1

                while have == need:
                    s1 = s[lp : rp + 1]
                    ln = len(s1)
                    if ln < mini:
                        mini = ln
                        ans = s1
                    d2[s[lp]] -= 1
                    if s[lp] in d1 and d2[s[lp]] < d1[s[lp]]:
                        have -= 1
                    lp += 1
                rp += 1
            return ans
