# title: word-search
# detail: https://leetcode.com/submissions/detail/146062186/
# datetime: Tue Mar 20 18:10:27 2018
# runtime: 438 ms
# memory: N/A

class Solution(object):
    def find(self, board, prev_pos, prev_idx, word):
        if prev_idx >= len(word) - 1:
            return True
        prev_m = prev_pos[0]
        prev_n = prev_pos[1]
        
        possible_pos = [[prev_m, prev_n - 1], [prev_m, prev_n + 1], [prev_m - 1, prev_n], [prev_m + 1, prev_n]]
        
        
        for m, n in possible_pos:
            if 0 <= m < self.m and \
                0 <= n < self.n and \
                board[m][n] == word[prev_idx + 1] and \
                self.board_paths[m][n] == 0:
                    
                self.board_paths[m][n] = 1
                
                if self.find(board, (m, n), prev_idx + 1, word):
                    return True
                self.board_paths[m][n] = 0
        return False
        
        
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.m = len(board)
        self.n = len(board[0])
        self.board_paths = [[0 for _ in range(self.n)] for _ in range(self.m)]
        
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] == word[0]:
                    self.board_paths[i][j] = 1
                    if self.find(board, (i, j), 0, word):
                        return True
                    self.board_paths[i][j] = 0
                    
        return False
        
        