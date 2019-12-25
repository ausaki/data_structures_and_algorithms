# title: number-of-islands
# detail: https://leetcode.com/submissions/detail/275320605/
# datetime: Sat Nov  2 23:45:02 2019
# runtime: 172 ms
# memory: 19.5 MB

class DisjSet:
    def __init__(self):
        self.elements = {}
        self.disj_set = []
        
    def add(self, x):
        if x not in self.elements:
            self.elements[x] = len(self.disj_set)
            self.disj_set.append(-1)
        
    def find(self, x):
        if x not in self.elements:
            return -1
        i = self.elements[x]
        while self.disj_set[i] >= 0:
            i = self.disj_set[i]
        return i
    
    def union(self, x, y):
        i = self.find(x)
        if i == -1:
            return
        j = self.find(y)
        if j == -1:
            return
        if i == j:
            return
        if self.disj_set[i] < self.disj_set[j]:
            self.disj_set[j] = i
        else:
            if self.disj_set[i] == self.disj_set[j]:
                self.disj_set[j] -= 1
            self.disj_set[i] = j
    
    def count_set(self):
        count = 0
        for i in self.disj_set:
            if i < 0:
                count += 1
        return count
    
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        if ROWS == 0:
            return 0
        COLS = len(grid[0])
        if COLS == 0:
            return 0
        disj_set = DisjSet()
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == '1':
                    disj_set.add((i, j))
                    if i - 1 >= 0 and grid[i - 1][j] == '1':
                        disj_set.union((i - 1, j), (i, j))
                    if j - 1 >= 0 and grid[i][j - 1] == '1':
                        disj_set.union((i, j - 1), (i, j))
        return disj_set.count_set()
                        
        
        