class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        list_of_squares = []
        for i in nums:
            num_square = i ** 2
            list_of_squares.append(num_square)
        return sorted(list_of_squares)
        