# title: game-of-life
# detail: https://leetcode.com/submissions/detail/284788503/
# datetime: Mon Dec  9 21:10:01 2019
# runtime: 32 ms
# memory: 12.8 MB

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        M = len(board)
        N = len(board[0])
        for i in range(M):
            for j in range(N):
                neighbors = [
                    [i, j - 1], [i, j + 1],
                    [i - 1, j], [i + 1, j],
                    [i - 1, j - 1], [i - 1, j + 1],
                    [i + 1, j - 1], [i + 1, j + 1]
                ]
                count = 0
                for ii, jj in neighbors:
                    if 0 <= ii < M and 0 <= jj < N and board[ii][jj] & 1:
                        count += 1
                if count < 2 or count > 3:
                    # death, do nothing
                    pass
                elif count == 2:
                    board[i][j] |= board[i][j] << 1
                elif count == 3:
                    board[i][j] = board[i][j] | 2
        for i in range(M):
            for j in range(N):
                board[i][j] >>= 1
        