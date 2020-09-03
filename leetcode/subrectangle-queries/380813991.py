# title: subrectangle-queries
# detail: https://leetcode.com/submissions/detail/380813991/
# datetime: Fri Aug 14 22:48:32 2020
# runtime: 148 ms
# memory: 15.8 MB

class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.matrix = rectangle
        self.rows = len(self.matrix)
        self.cols = len(self.matrix[0])
        self.layers = []

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        self.layers.append((row1 * self.cols + col1, row2 * self.cols + col2, newValue))

    def getValue(self, row: int, col: int) -> int:
        for p1,  p2, val in reversed(self.layers):
            r1, c1 = divmod(p1, self.cols)
            r2, c2 = divmod(p2, self.cols)
            if r1 <= row <= r2 and c1 <= col <= c2:
                return val
        return self.matrix[row][col]


# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)