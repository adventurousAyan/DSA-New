class Solution:

    # https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/

    def minDeletions(self, s: str) -> int:

        d1 = {}
        for ch in s:
            d1[ch] = d1.get(ch, 0) + 1

        min_dels = 0

        # Declare a set over here
        l1 = set()

        # Loop through the frequency dict
        for key in list(d1.keys()):
            # If the set doesnt contain frequency , add it
            if d1[key] not in l1:
                l1.add(d1[key])
            else:
                # Here the set already has a same frequency. Hence we decrease the freq count
                # such that the modified freq count, doesnt exist in the set. As we are decresing the
                # frequencies, we are incrementing the deletion count as well
                while d1[key] in l1:
                    if d1[key] != 0:
                        d1[key] -= 1
                        min_dels += 1
                    else:
                        break
                l1.add(d1[key])
        return min_dels
