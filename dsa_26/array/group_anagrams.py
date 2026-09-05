class Solution:
    # https://leetcode.com/problems/group-anagrams/
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        
        def is_anagram(w1, w2):
            d1 = {}

            if len(w1) != len(w2):
                return False

            for c in w1:
                d1[c] = d1.get(c, 0) + 1
            for c in w2:
                if c not in d1.keys():
                    return False
                d1[c] -= 1
                if d1[c] == 0:
                    d1.pop(c)
            return len(d1.keys()) == 0
          
        s1 = []
       
        for i in range(len(strs)):
            s2 = []
            for j in range(len(strs)):
                if is_anagram(strs[i], strs[j]):
                    if i != j:
                        s2.append(strs[j])
                    else:
                        s2.append(strs[i])
            s3 = sorted(s2)
            if s3 not in s1:
                s1.append(s3)
        return s1
    
# Above solution is not optimal, we can use a dictionary to group anagrams together by using sorted string as key and list of anagrams as value.







        