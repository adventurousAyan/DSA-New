# Given two strings first and second, consider occurrences in some text of the form "first second third", where second comes immediately after first, and third comes immediately after second.

# Return an array of all the words third for each occurrence of "first second third"

# Input: text = "alice is a good girl she is a good student", first = "a", second = "good"
# Output: ["girl","student"]


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:

        text_ls = text.split(" ")
        res = []
        n = len(text_ls)
        for i in range(len(text_ls)):
            if i + 2 < n and text_ls[i] == first and text_ls[i + 1] == second:
                res.append(text_ls[i + 2])
        return res
