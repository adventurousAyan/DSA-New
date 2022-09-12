# https://leetcode.com/problems/string-to-integer-atoi/


class Solution:
    def myAtoi(self, s: str) -> int:

        sign = 1
        char_start = False
        sign_found = False
        su = ""
        high, low = 2**31 - 1, -(2**31)
        for i in range(len(s)):
            # This is a case where string starts with a " " and a char or a sign hasnt been encountered
            if s[i] == " " and not char_start and not sign_found:
                continue
            # This is a case where the first sign has been encountered and no character encountered yet
            elif (s[i] == "-" or s[i] == "+") and not char_start and not sign_found:
                sign_found = True
                sign = -1 if s[i] == "-" else 1
            # Here character is encountered
            else:
                char_start = True
                if s[i].isdigit():
                    su += s[i]
                # Break as soon as the character found is not a digit
                else:
                    break
        if su == "":
            su = 0
        # Convert the resultant string and also add the sign
        su = sign * int(su)
        # Take care of boundary conditions
        if su < low:
            return low
        if su > high:
            return high
        return su
