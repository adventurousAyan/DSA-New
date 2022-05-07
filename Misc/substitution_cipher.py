from collections import OrderedDict


class Solution:

    # https://leetcode.com/discuss/interview-question/1966386/Coinbase-or-SDE2-or-OA-or-Karat-Interview

    def substitutionCipher(self, key: str, text: str) -> str:
        mydict = OrderedDict()
        d1 = {}

        # Generate alphabets from a-z
        alpha = [chr(x) for x in range(97, 123)]

        # Put ordered set of letters in dictionary only in the first occurance
        for val in key:
            val = val.lower()
            if val in alpha and val not in mydict and val != " ":
                mydict[val.upper()] = 1

        # Get the keys
        ls = mydict.keys()

        # For the keys map it to the original alphabets
        idx = 0
        for key in ls:
            if idx < 26:
                d1[alpha[idx].upper()] = key
                idx += 1
            else:
                idx = 0

        # Encode the string
        for i in range(len(text)):
            text = list(text)
            val = text[i]
            if val != " " and val.lower() in alpha:
                text[i] = d1[text[i].upper()] if i == 0 else d1[text[i].upper()].lower()
        text = "".join(text)

        return text

    def decrypt(self, dict, cipherText):
        # TODO: Need to complete this
        ls = self.solve(0, len(cipherText), cipherText, [])
        # print(ls)
        s = []
        for val in ls:
            x = len(set(val))
            y = [a for a in dict if len(set(a)) == x]
            s.append(y)
        return s

    def solve(self, j, n, s, ls):

        if j == n:
            return ls
        else:
            val1 = "0"
            val2 = "0"
            if j >= 0:
                val1 = s[: j + 1]
            if j + 1 < n:
                val2 = s[j + 1 :]
            if (
                list(val1)[0] != "0"
                and list(val2)[0] != "0"
                and (val1 != s or val2 != s)
            ):
                if len(val1) > 2:
                    l1 = self.solve(0, len(val1), val1, [])
                else:
                    l1 = [val1]
                if len(val2) > 2:
                    l2 = self.solve(0, len(val2), val2, [])
                else:
                    l2 = [val2]
                l1.extend(l2)
                if l1 not in ls:
                    ls.append(l1)
            return self.solve(j + 1, n, s, ls)


s = Solution()
print(
    s.substitutionCipher(
        "The quick onyx goblin, Grabbing his sword ==}-------- jumps over the 1st lazy dwarf!",
        "Would you kindly?",
    )
)
print(s.decrypt(["AXE", "CAT", "AT", "OR", "A", "COO", "CARD"], "123"))
