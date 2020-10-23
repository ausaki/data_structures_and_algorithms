# title: transform-to-chessboard
# detail: https://leetcode.com/submissions/detail/412307138/
# datetime: Sat Oct 24 00:55:40 2020
# runtime: 72 ms
# memory: 14.2 MB

class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        n = len(board)
        MASK = (1 << n) - 1
        ROW = 0
        for i in range(0, n, 2):
            ROW |= 1 << i
        cnt = collections.Counter(sum(1 << i for i, j in enumerate(r) if j) for r in board)
        if len(cnt) != 2:
            return -1
        (r1, k1), (r2, k2) = cnt.items()
        ones = bin(r1).count('1')
        if r1 != ~r2 & (MASK) or abs(k1 - k2) > 1 or abs(n - 2 * ones) > 1:
            return -1
        diff_bits = r1 ^ ROW
        row_diff = bin(diff_bits).count('1')
        if row_diff % 2 or ((n - row_diff) % 2 == 0 and n - row_diff < row_diff):
            row_diff = n - row_diff
        col = sum(1 << i for i in range(n) if board[i][0])
        diff_bits = col ^ ROW
        col_diff = bin(diff_bits).count('1')
        if col_diff % 2 or ((n - col_diff) % 2 == 0 and n - col_diff < col_diff):
            col_diff = n - col_diff
        return (row_diff + col_diff) // 2
        