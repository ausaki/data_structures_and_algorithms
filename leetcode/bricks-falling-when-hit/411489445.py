# title: bricks-falling-when-hit
# detail: https://leetcode.com/submissions/detail/411489445/
# datetime: Wed Oct 21 23:24:06 2020
# runtime: 744 ms
# memory: 23.2 MB

class DisjSet:
    def __init__(self, n ):
        self.disj_set = [-1] * n
        self.disj_sizes = [1] * n
        
    def find(self, x):
        while self.disj_set[x] >= 0:
            x = self.disj_set[x]
        return x
    
    def union(self, x, y):
        i = self.find(x)
        j = self.find(y)
        if i == j:
            return -1
        if self.disj_set[i] < self.disj_set[j]:
            self.disj_set[j] = i
            self.disj_sizes[i] += self.disj_sizes[j]
            self.disj_sizes[j] = 0
            return i
        if self.disj_set[i] == self.disj_set[j]:
            self.disj_set[j] -= 1
        self.disj_set[i] = j
        self.disj_sizes[j] += self.disj_sizes[i]
        self.disj_sizes[i] = 0
        return j
    
    def get_size(self, x):
        return self.disj_sizes[self.find(x)]
    
    def get_size2(self, x):
        return self.disj_sizes[x]
    
class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        disj = DisjSet(m * n)
        for i, j in hits:
            grid[i][j] -= 2
        for i in range(m):
            for j in range(n):
                p = i * n + j
                if grid[i][j] <= 0:
                    continue
                if i and grid[i - 1][j] == 1:
                    disj.union(p, p - n)
                if j and grid[i][j - 1] == 1:
                    disj.union(p, p - 1)
        top_set = set()
        for j in range(n):
            if grid[0][j] == 1:
                top_set.add(disj.find(j))
                
        result = [0] * len(hits)
        for k in range(len(hits) - 1, -1, -1):
            i, j = hits[k]
            grid[i][j] += 2
            if grid[i][j] == 0:
                result[k] = 0
                continue
            if i == 0:
                top_set.add(disj.find(j))
            neighbors = set()
            connected = False
            sz = 0
            for di, dj in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
                ii, jj = i + di, j + dj
                if 0 <= ii < m and 0 <= jj < n and grid[ii][jj] == 1:
                    p = ii * n + jj
                    s1 = disj.find(p)
                    if s1 not in top_set:
                        if s1 not in neighbors:
                            sz += disj.disj_sizes[s1]
                    else:
                        connected = True
                    neighbors.add(s1)
            if i * n + j in top_set:
                connected = True
                top_set.discard(i * n + j)
            new_set = i * n + j
            for nb in neighbors:
                if nb in top_set:
                    top_set.discard(nb)
                s = disj.union(i * n + j, nb)
                if s != -1:
                    new_set = s
            if connected:
                result[k] = sz
                top_set.add(new_set)
        return result
                        