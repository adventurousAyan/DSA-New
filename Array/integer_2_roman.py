class Solution:
    def intToRoman(self, num: int) -> str:

        d1 = {}
        # Store all inum to  roman mappings in a dictionary. This will include the differencing as well
        d1[1] = "I"
        d1[4] = "IV"
        d1[5] = "V"
        d1[9] = "IX"
        d1[10] = "X"
        d1[40] = "XL"
        d1[50] = "L"
        d1[90] = "XC"
        d1[100] = "C"
        d1[400] = "CD"
        d1[500] = "D"
        d1[900] = "CM"
        d1[1000] = "M"
        ls = sorted(d1.keys())

        def f(ls, num, ans):

            # If Num is 0, we got our ans
            if num == 0:
                return ans
            # If number is a part of dictionary key, append it to ans and return
            if num in d1:
                ans += d1[num]
                return ans

            # Do Binary Search
            start = 0
            end = len(ls) - 1
            floor = -1
            while start <= end:
                mid = start + (end - start) // 2
                if num > ls[mid]:
                    floor = mid
                    start = mid + 1
                elif num < ls[mid]:
                    end = mid - 1
            # Get the floor value
            val = ls[floor]
            # If number is greater than highest range
            if num > 1000:
                ans += d1[1000] * (num // 1000)
                num = num % 1000
            else:
                # We need to divide the num by floor value and the quotient will be the number of roman
                # characters needed for that value
                ans += d1[val] * (num // val)
                num = num % val
            return f(ls, num, ans)

        return f(ls, num, "")
