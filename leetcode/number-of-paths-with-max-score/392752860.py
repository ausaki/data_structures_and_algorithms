# title: number-of-paths-with-max-score
# detail: https://leetcode.com/submissions/detail/392752860/
# datetime: Tue Sep  8 17:30:39 2020
# runtime: 136 ms
# memory: 13.9 MB

class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        m = len(board)
        n = len(board[0])
        MOD = 10 ** 9 + 7
        dp = []
        for i in range(m):
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
                for s, p in [(dp2[j - 1] if j > 0 else [0,0]), (dp[j - 1] if i > 0 and j > 0 else [0, 0]), (dp[j] if i > 0 else [0, 0])]:
                    if p > 0:
                        if s > maxsum:
                            maxsum = s
                            path = p
                        elif s == maxsum:
                            path = (path + p) % MOD
                dp2.append([maxsum + int(board[i][j] if board[i][j].isdigit() else 0), path])
            dp = dp2
        return dp[n - 1]