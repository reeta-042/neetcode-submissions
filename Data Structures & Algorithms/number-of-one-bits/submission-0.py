class Solution:
    def hammingWeight(self, n: int) -> int:

        total = 0

        while n > 0:
            if n & 1 != 0:
                total += 1

            n = n >> 1

        return total
        

        