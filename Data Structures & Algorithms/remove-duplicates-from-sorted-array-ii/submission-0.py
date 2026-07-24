class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 2
        for i in range(2,len(nums)):
            if nums[i] != nums[slow -2]:
                nums[slow] = nums[i]
                slow += 1
        return slow
        