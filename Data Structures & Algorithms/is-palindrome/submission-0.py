class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = "".join(char for char in s if char.isalnum()).lower()
        reverse_word = word[::-1]

        return word == reverse_word
            

        