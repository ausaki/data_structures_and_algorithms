# title: find-winner-on-a-tic-tac-toe-game
# detail: https://leetcode.com/submissions/detail/393687133/
# datetime: Thu Sep 10 17:43:47 2020
# runtime: 36 ms
# memory: 13.9 MB

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
        rows.extend(cols)
        rows.extend(dia)
        if 3 in rows:
            return 'A'
        if 12 in rows:
            return 'B'
        if len(moves) == 9:
            return 'Draw'
        return 'Pending'
        