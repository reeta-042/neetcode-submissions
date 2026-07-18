class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows, columns = len(matrix),len(matrix[0])
        output = [[0] * rows for i in range(columns)]

        for r in range(rows):
            for c in range(columns):
                output[c][r] = matrix[r][c]
        return output    

        