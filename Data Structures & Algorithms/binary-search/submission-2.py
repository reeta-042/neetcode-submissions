class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        stop = len(nums) - 1

        while start <= stop:
             mid = (start + stop) // 2
             if nums[mid] ==  target:
                return mid
             elif nums[mid] < target: 
                start = mid + 1
             else:
                stop = mid - 1
        return -1

            

        