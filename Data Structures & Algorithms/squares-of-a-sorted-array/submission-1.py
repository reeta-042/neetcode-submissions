class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        first,last = 0, len(nums) - 1
        list_of_numbers = []
        while first <= last:
            if abs(nums[last]) > abs(nums[first]):
                j = nums[last] ** 2
                list_of_numbers.append(j)
                last -= 1
            else:
                j = nums[first] ** 2
                list_of_numbers.append(j)
                first += 1
        return sorted(list_of_numbers)
        