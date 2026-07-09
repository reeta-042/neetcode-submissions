class Solution:
    def missingNumber(self, nums: List[int]) -> int:

       
        length = len(nums) + 1
        boundary = list(range(length))
        for n in boundary:
            if n not in nums:
                return n


        