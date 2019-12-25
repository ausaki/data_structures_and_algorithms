# title: valid-tic-tac-toe-state
# detail: https://leetcode.com/submissions/detail/282871617/
# datetime: Sun Dec  1 13:26:36 2019
# runtime: 24 ms
# memory: 12.5 MB

class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        def check(c):
            for i in range(3):
                if board[i].count(c) == 3:
                    return True
                if board[0][i] == c and board[1][i] == c and board[2][i] == c:
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
