class Solution:
    """The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

            P   A   H   N
            A P L S I I G
            Y   I   R
            And then read line by line: "PAHNAPLSIIGYIR"

            Write the code that will take a string and make this conversion given a number of rows:

            string convert(string s, int numRows);

            https://leetcode.com/problems/zigzag-conversion/
    """
    def convert(self, s: str, numRows: int) -> str:
        i = 0
        j = numRows - 1
        ls = []
        t = 0
        n = len(s)
        if numRows == 1:
            return s
        while j < n:
            s1 = []
            while i <= j:
                s1.append(s[i])
                i = i + 1
            temp = "".join([str(x) for x in s1])
            ls.append(temp)
            temp = ""
            t = j
            j = j+numRows -1
            i = i-1
        if t<n:
            ls.append(s[t:])
        for x in range(len(ls)):
            if x%2 != 0:
                diag = ls[x]
                if len(diag) < numRows:
                    sub_diag = diag[1:]
                else:
                    sub_diag = diag[1:-1]
                print(sub_diag)
                rev_diag = sub_diag[::-1]
                rev_diag = rev_diag.rjust(numRows-1, '0')
                rev_diag = rev_diag.ljust(numRows, '0')
                ls[x] = rev_diag
        cols = len(ls)
        k = [[0]*(n) for i in range(numRows)]
        for i in range(len(ls)):
            if i%2 == 0:
                l1 = len(ls[i])
                if l1 < numRows:
                    ls[i] = ls[i].ljust(numRows, '0')      
                    
        for i in range(numRows):
            for j in range(cols):
                    if ls[j]:
                        k[i][j] = ls[j][i]       
        
        res = ""
        for i in range(numRows):
            for j in range(cols):
                if k[i][j] != '0':
                    res = res + k[i][j]
        return res
        