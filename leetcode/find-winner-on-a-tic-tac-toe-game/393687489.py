# title: find-winner-on-a-tic-tac-toe-game
# detail: https://leetcode.com/submissions/detail/393687489/
# datetime: Thu Sep 10 17:45:24 2020
# runtime: 32 ms
# memory: 13.8 MB

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        rows = [0] * 3
        cols = [0] * 3
        dia = [0, 0]
        for p, (i, j) in enumerate(moves):
            a = 1 if p % 2 == 0 else 4
            rows[i] += a
            cols[j] += a
            if i == j:
                dia[0] += a
            if i + j == 2:
                dia[1] += a
            if 3 == rows[i] or 3 == cols[j] or 3 == dia[0] or 3 == dia[1]:
                return 'A'
            if 12 == rows[i] or 12 == cols[j] or 12 == dia[0] or 12 == dia[1]:
                return 'B'
        if len(moves) == 9:
            return 'Draw'
        return 'Pending'
        