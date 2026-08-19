class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        stop = len(nums) - 1

        while start <= stop:
            mid = (start + stop) //2
            if nums[mid] == target:
                return mid
            if nums[start] <= nums[mid]:
                if target >= nums[start] and target <= nums[mid]:
                    stop = mid - 1
                else:
                    start = mid + 1
            elif nums[mid] <= nums[stop]:
                if target >= nums[mid] and target <= nums[stop]:
                    start = mid + 1
                else:
                    stop = mid - 1 
        return - 1
        