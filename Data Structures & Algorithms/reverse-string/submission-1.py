class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        first = 0
        last = len(s) - 1
        while last > first:
            s[last],s[first] = s[first],s[last]

            first += 1
            last -= 1
        