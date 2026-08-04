class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashset = {}
        for num in nums:
            hashset[num] = hashset.get(num,0) +1
        return max(hashset,key = hashset.get)
            




        
        