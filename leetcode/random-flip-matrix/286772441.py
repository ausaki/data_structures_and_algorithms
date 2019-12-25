# title: random-flip-matrix
# detail: https://leetcode.com/submissions/detail/286772441/
# datetime: Wed Dec 18 11:09:25 2019
# runtime: 52 ms
# memory: 13.1 MB

import random
class Solution:

    def __init__(self, n_rows: int, n_cols: int):
        self.M = n_rows
        self.N = n_cols
        self.size = self.M * self.N
        self.matrix = {}
        
    def flip(self) -> List[int]:
        x = random.randrange(0, self.size)
        self.size -= 1
        k = self.matrix.get(x, x)
        self.matrix[x] = self.matrix.get(self.size, self.size)
        i, j = divmod(k, self.N)
        return [i, j]

    def reset(self) -> None:
        self.matrix.clear()
        self.size = self.M * self.N


# Your Solution object will be instantiated and called as such:
# obj = Solution(n_rows, n_cols)
# param_1 = obj.flip()
# obj.reset()