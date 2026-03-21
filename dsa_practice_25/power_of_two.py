class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
    # Using Bit Manipulation
    # Intuition - 16 - 10000 , 15 is 01111. & operation for both of them yields 0, for non powers of two, it yields a non zero number
    # For sample problems for bit manipulation follow this playlist - https://www.youtube.com/watch?v=nttpF8kwgd4&list=PLgUwDviBIf0rnqh8QsJaHyIX7KUiaPUv7&index=2
    
        if n == 0:
            return False

        return n & (n - 1) == 0
