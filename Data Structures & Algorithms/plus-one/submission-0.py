class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sum = int("".join(map(str,digits))) + int(1)
        return [int(i) for i in str(sum)] 
        