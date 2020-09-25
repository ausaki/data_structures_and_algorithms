# title: number-of-paths-with-max-score
# detail: https://leetcode.com/submissions/detail/392753582/
# datetime: Tue Sep  8 17:33:33 2020
# runtime: 128 ms
# memory: 13.9 MB

class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n = len(board)
        MOD = 10 ** 9 + 7
        dp = []
        for i in range(n):
            dp2 = []
            for j in range(n):
                if board[i][j] == 'X':
                    dp2.append([0, 0])
                    continue
                if board[i][j] == 'E':
                    dp2.append([0, 1])
                    continue
                maxsum = 0
                path = 0
                for s, p in [dp2[j - 1] if j else [0, 0], dp[j - 1] if i and j else [0, 0], dp[j] if i else [0, 0]]:
                    if p > 0:
                        if s > maxsum:
                            maxsum = s
                            path = p
                        elif s == maxsum:
                            path = (path + p) % MOD
                dp2.append([maxsum + int(board[i][j] if board[i][j].isdigit() else 0), path])
            dp = dp2
        return dp[n - 1]