# title: range-sum-query-2d---immutable
# detail: https://leetcode.com/submissions/detail/284802971/
# datetime: Mon Dec  9 23:07:44 2019
# runtime: 120 ms
# memory: 15.8 MB

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.M = len(self.matrix)
        if self.M == 0:
            self.N = 0
        else:
            self.N = len(self.matrix[0])
        self.cache = [[0 for j in range(self.N + 1)] for i in range(self.M + 1)]
        
        self.calc()
        
    def calc(self):
        for i in range(1, self.M + 1):
            for j in range(1, self.N + 1):
                self.cache[i][j] = (self.matrix[i - 1][j - 1] + 
                                    self.cache[i][j - 1] + 
                                    self.cache[i - 1][j] - 
                                    self.cache[i - 1][j - 1])
    
            
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (self.cache[row2 + 1][col2 + 1] - 
                self.cache[row2 + 1][col1] - 
                self.cache[row1][col2 + 1] +
                self.cache[row1][col1])

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)