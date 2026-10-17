class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.prefix = []
        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(0)
            self.prefix.append(row)
        for r in range(rows):
            for c in range(cols):
                if r == 0 and c == 0:
                    self.prefix[r][c] = matrix[r][c]
                elif c == 0:
                    self.prefix[r][c] = matrix[r][c] + self.prefix[r-1][c]

                elif r == 0:
                    self.prefix[r][c] = matrix[r][c] + self.prefix[r][c-1]

                else:
                    self.prefix[r][c] = matrix[r][c] + self.prefix[r-1][c] + self.prefix[r][c-1] - self.prefix[r-1][c-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = self.prefix[row2][col2]

        if row1 > 0:
            total -= self.prefix[row1 - 1][col2]

        if col1 > 0:
            total -= self.prefix[row2][col1 - 1]

        if row1 > 0 and col1 > 0:
            total += self.prefix[row1 - 1][col1 - 1]

        return total


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)