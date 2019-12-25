# title: battleships-in-a-board
# detail: https://leetcode.com/submissions/detail/285688740/
# datetime: Fri Dec 13 20:23:30 2019
# runtime: 96 ms
# memory: 13.4 MB

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        M = len(board)
        if M == 0: return 0
        N = len(board[0])
        res = 0
        for i in range(M):
            for j in range(N):
                print(i, j)
                if board[i][j] != '.':
                    continue
                if ((j - 1 >= 0 and board[i][j - 1] == 'X') and
                    ((i + 1 >= M or board[i + 1][j - 1] == '.') and 
                     (i - 1 < 0 or board[i - 1][j - 1] == '.'))):
                    res += 1
                cnt = 0
                for k in range(i - 2, i):
                    if k >= 0 and board[k][j] == 'X' and (j - 1 < 0 or board[k][j - 1] == '.') and (j + 1 >= N or board[k][j + 1] == '.'):
                        cnt += 1
                if cnt == 2:
                    res += 1
        j = N 
        for i in range(M):
            if ((j - 1 >= 0 and board[i][j - 1] == 'X') and
                ((i + 1 >= M or board[i + 1][j - 1] == '.') and 
                (i - 1 < 0 or board[i - 1][j - 1] == '.'))):
                res += 1
        i = M
        for j in range(N):
            cnt = 0
            for k in range(i - 2, i):
                if k >= 0 and board[k][j] == 'X' and (j - 1 < 0 or board[k][j - 1] == '.') and (j + 1 >= N or board[k][j + 1] == '.'):
                    cnt += 1
            if cnt == 2:
                res += 1
        return res
                