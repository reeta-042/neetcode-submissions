class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        max_num = counter = 0

        for i in nums:
            if i != 0:
                counter += 1
            else:
                counter = 0
            max_num = max(max_num,counter)
        return max_num
        




        