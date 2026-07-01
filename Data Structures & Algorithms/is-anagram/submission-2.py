class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        split_s = list(s)
        split_t = list(t)

        if len(split_s) != len(split_t):
            return False
        return sorted(split_s) == sorted(split_t)