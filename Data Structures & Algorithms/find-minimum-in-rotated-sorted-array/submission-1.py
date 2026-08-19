class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        start = 0
        stop = n -1

        while start < stop:
            mid = (start + stop) // 2
            if nums[mid] > nums[stop]:
                start = mid + 1
            else:
                stop = mid 
        return nums[start]

        