# title: valid-tic-tac-toe-state
# detail: https://leetcode.com/submissions/detail/282870529/
# datetime: Sun Dec  1 13:21:28 2019
# runtime: 20 ms
# memory: 12.9 MB

class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        def check(c):
            for i in range(3):
                for j in range(3):
                    if board[i][j] != c:
                        break
                else:
                    return True
            for i in range(3):
                for j in range(3):
                    if board[j][i] != c:
                        break
                else:
                    return True
            if board[0][0] == c and board[1][1] == c and board[2][2] == c:
                return True
            if board[0][2] == c and board[1][1] == c and board[2][0] == c:
                return True
            return False
        x = 0
        o = 0
        for row in board:
            x += row.count('X')
            o += row.count('O')
        if x == o:
            if x < 3:
                return True
            return not check('X')
        if x - o == 1:
            if x < 4:
                return True
            return not check('O')
        return False
