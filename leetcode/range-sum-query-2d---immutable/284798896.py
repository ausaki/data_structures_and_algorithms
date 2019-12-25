# title: range-sum-query-2d---immutable
# detail: https://leetcode.com/submissions/detail/284798896/
# datetime: Mon Dec  9 22:37:24 2019
# runtime: 612 ms
# memory: 14.9 MB

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.M = len(self.matrix)
        if self.M == 0:
            self.N = 0
        else:
            self.N = len(self.matrix[0])
        self.row = [0] * self.M
        self.col = [0] * self.N
        
        self.calc_row_sum()
        self.calc_col_sum()
        
    def calc_row_sum(self):
        for i in range(self.M):
            self.row[i] = sum(self.matrix[i])
    
    def calc_col_sum(self):
        for j in range(self.N):
            self.col[j] = sum(self.matrix[i][j] for i in range(self.M))
            
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        use_row_cache = col2 - col1 + 1 > (self.N // 2)
        use_col_cache = row2 - row1 + 1 > (self.M // 2)
        if use_row_cache:
            for i in range(row1, row2 + 1):
                res += self.row[i] - sum(self.matrix[i][0:col1]) - sum(self.matrix[i][col2 + 1:])
        elif use_col_cache:
            for j in range(col1, col2 + 1):
                s1 = sum(self.matrix[i][j] for i in range(row1))
                s2 = sum(self.matrix[i][j] for i in range(row2 + 1, self.M))
                res += self.col[j] - s1 - s2
        else:
            for i in range(row1, row2 + 1):
                res += sum(self.matrix[i][col1: col2 + 1])
        return res            


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)