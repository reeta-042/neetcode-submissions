class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r = 0
        n = len(nums)
        for i in range(n):
            if nums[i] != 0:
                nums[i],nums[r] = nums[r],nums[i]
                r += 1
        
