class Solution:
    def missingNumber(self, nums: List[int]) -> int:

         n = len(nums) + 1
         x = list(range(n))

         result = set(x) - set(nums)

         return list(result)[0]
        