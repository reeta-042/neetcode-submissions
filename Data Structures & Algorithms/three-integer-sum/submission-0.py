class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        list_of_three = []

        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            f, l = i + 1,len(nums) - 1
            while f < l:
                three_sum = nums[i] + nums[f] + nums[l]
                if three_sum == 0:
                    list_of_three.append([nums[i],nums[f],nums[l]])
                    f += 1
                    while f < l and nums[f] == nums[f-1]:
                        f+=1
                elif three_sum < 0:
                    f += 1
                else:
                    l -= 1
        return list_of_three
        