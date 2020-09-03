# title: subrectangle-queries
# detail: https://leetcode.com/submissions/detail/380812897/
# datetime: Fri Aug 14 22:45:04 2020
# runtime: 152 ms
# memory: 15.9 MB

class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.matrix = rectangle
        self.layers = []

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        self.layers.append((row1, col1, row2, col2, newValue))

    def getValue(self, row: int, col: int) -> int:
        for r1, c1,  r2, c2, val in reversed(self.layers):
            if r1 <= row <= r2 and c1 <= col <= c2:
                return val
        return self.matrix[row][col]


# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)