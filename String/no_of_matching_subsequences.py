from collections import defaultdict
from typing import List


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:

        d1 = {}

        for word in words:
            d1[word] = d1.get(word, 0) + 1

        n = len(s)
        l1 = set()
        cnt = 0
        for num in range(1 << n):
            sub = ""
            for i in range(n):
                if (1 << i) & num != 0:
                    sub += s[i]

            if d1.get(sub, 0) > 0 and sub not in l1:
                l1.add(sub)
                cnt += d1[sub]
        return cnt


###################### 2nd approach ##############################################

# I begin by creating a default dictionary of 'list' objects. The main benefit of a default dictionary is that when you access an entry that does not yet exist,
# the entry is created automatically (in this case, the value for the entry is an empty list when it is created).
# I then create a 'count' variable to keep track of the number of words that are subsequences of the given string.

# The first thing I do with the dictionary is populate it with all the words in the list of words.
# The key for each entry is the first letter of the word.
# The value is the list of words that start with that letter.
# Using the example in the problem, the dictionary would look like the following:

# {'a': ['a', 'acd', 'ace'], 'b': ['bb']}

# The next step is to iterate through each character in the given string.
# For each character, I access the dictionary to retrieve the list of words that start with that character.
# I reset the value of the entry to an empty list and then iterate through the list of words I retrieved. If the word is only a single letter, 
# then I conclude that we have successfully found a completed subsequence and increase our 'count' by one. Otherwise, 
# I slice off the first character and add the sliced word back to the dictionary. This time, it is added to the entry for which the key is equal to 
# the first letter of the sliced word.

# This process continues until we have iterated through all characters in the string.
# At the end, I return the count.


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:

        d1 = defaultdict(list)

        for word in words:
            d1[word[0]].append(word)

        cnt = 0
        for ch in s:
            wrds = d1[ch]
            d1.pop(ch)
            for wrd in wrds:
                if wrd.startswith(ch):
                    w1 = wrd[1 : len(wrd)]
                    if w1 == "":
                        cnt += 1
                    else:
                        d1[w1[0]].append(w1)

        return cnt
