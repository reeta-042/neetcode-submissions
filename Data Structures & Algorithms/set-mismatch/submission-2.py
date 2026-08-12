class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        return_list = [0, 0] 
        count = Counter(nums)

        for i in range(1, len(nums) + 1):
            if count[i] == 0:
                return_list[1] = i
            if count[i] == 2:
                return_list[0] = i

        return return_list

        