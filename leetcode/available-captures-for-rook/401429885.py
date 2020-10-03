# title: available-captures-for-rook
# detail: https://leetcode.com/submissions/detail/401429885/
# datetime: Mon Sep 28 00:06:49 2020
# runtime: 24 ms
# memory: 14.1 MB

class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        n = 8
        result = 0
        for i in range(n):
            for j in range(n):
                if board[i][j] != 'R':
                    continue
                for y in range(j - 1, -1, -1):
                    if board[i][y] == '.':
                        continue
                    if board[i][y] == 'p':
                        result += 1
                    break
                for y in range(j + 1, n):
                    if board[i][y] == '.':
                        continue
                    if board[i][y] == 'p':
                        result += 1
                    break
                for x in range(i - 1, -1, -1):
                    if board[x][j] == '.':
                        continue
                    if board[x][j] == 'p':
                        result += 1
                    break
                for x in range(i + 1, n):
                    if board[x][j] == '.':
                        continue
                    if board[x][j] == 'p':
                        result += 1
                    break
        return result