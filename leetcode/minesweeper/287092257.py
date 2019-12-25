# title: minesweeper
# detail: https://leetcode.com/submissions/detail/287092257/
# datetime: Thu Dec 19 18:24:16 2019
# runtime: 204 ms
# memory: 15.3 MB

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def update(i, j):
            if board[i][j] == 'M':
                board[i][j] = 'X'
                return
            if board[i][j] != 'E':
                return
            m = 0
            for ii in range(i - 1, i + 2):
                for jj in range(j - 1, j + 2):
                    if 0 <= ii < M and 0 <= jj < N and (ii != i or jj != j):
                        if board[ii][jj] == 'M':                            
                            m += 1
            if m > 0:
                board[i][j] = str(m)
                return
            board[i][j] = 'B'
            for ii in range(i - 1, i + 2):
                for jj in range(j - 1, j + 2):
                    if 0 <= ii < M and 0 <= jj < N and (ii != i or jj != j):
                        update(ii, jj)
                
        M = len(board)
        if M == 0:
            return board
        N = len(board[0])
        update(*click)
        return board