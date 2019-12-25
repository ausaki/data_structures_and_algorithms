# title: stone-game
# detail: https://leetcode.com/submissions/detail/276187206/
# datetime: Tue Nov  5 19:07:19 2019
# runtime: 724 ms
# memory: 19.8 MB

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        N = len(piles)
        # return self._play(piles, 0, N - 1, 0, [0, 0])
        return self._play2(piles)
        
    def _play(self, piles, start, end, player, scores):
        '''recursive'''
        if start >= end:
            # game is over
            return scores[0] > scores[1]
        next_player = (player + 1) % 2
        s1 = list(scores)
        s1[player] += piles[start]
        res1 = self._play(piles, start + 1, end, next_player, s1)
        s2 = list(scores)
        s2[player] += piles[end]
        res2 = self._play(piles, start, end - 1, next_player, s2)
        if player == 0:
            return res1 or res2
        else:
            return res1 and res2
    
    def _play2(self, piles):
        '''DP'''
        N = len(piles)
        dp = [[0 for _ in range(N)] for _ in range(N)]
        
        for i in range(N - 1):
            dp[i][i + 1] = max(piles[i], piles[i + 1])
        
        for i in reversed(range(N - 3)):
            for j in range(i + 3, N):
                dp[i][j] = max(
                    dp[i + 2][j] + piles[i] if i + 2 < N else 0,
                    dp[i + 1][j - 1] + piles[i] if i + 1 < N and j - 1 >= 0 else 0,
                    dp[i][j - 2] + piles[j] if j - 2 >= 0 else 0,
                    dp[i + 1][j - 1] + piles[j] if i + 1 < N and j - 1 >= 0 else 0,
                )
        return dp[0][N - 1] > sum(piles) / 2