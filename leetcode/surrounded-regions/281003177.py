# title: surrounded-regions
# detail: https://leetcode.com/submissions/detail/281003177/
# datetime: Sat Nov 23 14:10:04 2019
# runtime: 300 ms
# memory: 17.8 MB

class DisjSet:
    def __init__(self):
        self.elements = {}
        self.disj_set = []
        
    def add(self, x):
        if x not in self.elements:
            self.elements[x] = len(self.disj_set)
            self.disj_set.append(-1)
            return self.elements[x]
        return -1
        
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
            return - 1
        j = self.find(y)
        if j == -1:
            return -1
        if i == j:
            return i
        if self.disj_set[i] < self.disj_set[j]:
            self.disj_set[j] = i
            return i
        else:
            if self.disj_set[i] == self.disj_set[j]:
                self.disj_set[j] -= 1
            self.disj_set[i] = j
            return j
    
    def count_set(self):
        count = 0
        for i in self.disj_set:
            if i < 0:
                count += 1
        return count
        
        
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        disj_set = DisjSet()
        N = len(board)
        if N == 0:
            return 
        M = len(board[0])
        if M == 0:
            return
        for i in range(N):
            for j in range(M):
                if board[i][j] == 'X':
                    continue
                k = i * M + j
                disj_set.add(k)
                if j - 1 >= 0 and board[i][j - 1] == 'O':
                    disj_set.union(k, i * M + j - 1)
                if i - 1 >= 0 and board[i - 1][j] == 'O':
                    disj_set.union(k, (i - 1) * M + j)
        regions = set()
        for i in range(N):
            for j in range(M):
                if board[i][j] == 'O' and (i == 0 or i == N -1 or j == 0 or j == M - 1):
                    regions.add(disj_set.find(i * M + j))
        for i in range(N):
            for j in range(M):
                if board[i][j] == 'O':
                    if disj_set.find(i * M + j) not in regions:
                        board[i][j] = 'X'
                    
        
                        
        
        