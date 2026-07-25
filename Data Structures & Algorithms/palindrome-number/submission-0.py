class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = list(str(x))
        reverse_num = num[::-1]
        return num == reverse_num
        