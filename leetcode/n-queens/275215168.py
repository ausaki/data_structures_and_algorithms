# title: n-queens
# detail: https://leetcode.com/submissions/detail/275215168/
# datetime: Sat Nov  2 10:51:42 2019
# runtime: 56 ms
# memory: 13.9 MB

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.solutions = []
        self.solution = []
        col = [0] * n
        pie = [0] * 2 * n
        na = [0] * 2 * n
        self._solve(0, col, pie, na)
        return self.solutions
    
    def _solve(self, row, col, pie, na):
        n = len(col)
        if row == n:
            solution = [None] * n
            for i in range(n):
                r = -col[i] - 1
                solution[r] = '.' * i + 'Q' + '.' * (n - i - 1)
            self.solutions.append(solution)
            return
        for c in range(n):
            if col[c] == 0 and pie[row + c] == 0 and na[row - c] == 0:
                col[c] = -row - 1
                pie[row + c] = 1
                na[row - c] = 1
                self._solve(row + 1, col, pie, na)
                col[c] = 0
                pie[row + c] = 0
                na[row - c] = 0
