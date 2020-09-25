# title: find-winner-on-a-tic-tac-toe-game
# detail: https://leetcode.com/submissions/detail/393685040/
# datetime: Thu Sep 10 17:34:41 2020
# runtime: 36 ms
# memory: 13.9 MB

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        g = [[0] * 3 for i in range(3)]
        for p, (i, j) in enumerate(moves):
            a = 1 if p % 2 == 0 else 4
            g[i][j] = a
        for i in range(3):
            s1 = sum(g[i])
            s2 = sum(g[j][i] for j in range(3))
            if s1 == 3 or s2 == 3:
                return 'A'
            if s1 == 12 or s2 == 12:
                return 'B'
        s1 = g[0][0] + g[1][1] + g[2][2]
        s2 = g[2][0] + g[1][1] + g[0][2]
        if s1 == 3 or s2 == 3:
            return 'A'
        if s1 == 12 or s2 == 12:
            return 'B'
        if len(moves) == 9:
            return 'Draw'
        return 'Pending'
        