# title: number-of-islands
# detail: https://leetcode.com/submissions/detail/275314442/
# datetime: Sat Nov  2 23:15:36 2019
# runtime: 196 ms
# memory: 19.3 MB

class DisjSet:
    def __init__(self):
        self.elements = {}
        self.disj_set = []
        
    def add(self, x):
        if x not in self.elements:
            self.elements[x] = len(self.disj_set)
            self.disj_set.append(-1)
        
    def find(self, x):
        i = self.elements[x]
        while self.disj_set[i] >= 0:
            i = self.disj_set[i]
        return i
    
    def union(self, x, y):
        i = self.find(x)
        j = self.find(y)
        if i == j:
            return
        self.disj_set[j] = i
    
    def count_set(self):
        count = 0
        for i in self.disj_set:
            if i == -1:
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
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == '1':
                    if i - 1 >= 0 and grid[i - 1][j] == '1':
                        disj_set.union((i, j), (i - 1, j))
                    if i + 1 < ROWS and grid[i + 1][j] == '1':
                        disj_set.union((i, j), (i + 1, j))
                    if j - 1 >= 0 and grid[i][j - 1] == '1':
                        disj_set.union((i, j), (i, j - 1))
                    if j + 1 < COLS and grid[i][j + 1] == '1':
                        disj_set.union((i, j), (i, j + 1))
        return disj_set.count_set()
                        
        
        