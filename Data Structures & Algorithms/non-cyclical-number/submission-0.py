class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        cur = str(n)

        while cur not in seen:
            seen.add(cur)
            summ = 0
            for digit in cur:
                digit = int(digit)
                summ += digit * digit
            if summ == 1:
                return True
            cur = str(summ)
        return False
        
        