class Solution:
    def countCommas(self, n: int) -> int:
        if n <= 998:
            return 0
        else:
            return n-999