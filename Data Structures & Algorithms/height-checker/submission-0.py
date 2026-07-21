class Solution:
    def heightChecker(self, heights: List[int]) -> int:

        counter = 0
        n = len(heights) 

        expected = sorted(heights)

        for i in range(n):
            if heights[i] != expected[i]:
                counter += 1

        return counter

        