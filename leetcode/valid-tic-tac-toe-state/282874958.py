# title: valid-tic-tac-toe-state
# detail: https://leetcode.com/submissions/detail/282874958/
# datetime: Sun Dec  1 13:42:34 2019
# runtime: 28 ms
# memory: 12.7 MB

class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        def check(c):
            row = [0] * 3
            col = [0] * 3
            dia1 = 0
            dia2 = 0
            for i in range(3):
                for j in range(3):
                    if board[i][j] == c:
                        row[i] += 1
                        col[j] += 1
                        if i == j:
                            dia1 += 1
                        if i + j == 2:
                            dia2 += 1
            if dia1 == 3 or dia2 == 3 or any(map(lambda i: i == 3, row)) or any(map(lambda i: i == 3, col)):
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
