# title: stone-game
# detail: https://leetcode.com/submissions/detail/276202045/
# datetime: Tue Nov  5 21:26:50 2019
# runtime: 424 ms
# memory: 19.3 MB

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
        
        
        for i in reversed(range(N)):
            dp[i][i] = -piles[i]
            for j in range(i + 1, N):
                player = (j - i + 1) % 2
                if player == 0:
                    # first player: alex
                    dp[i][j] = max(piles[i] + dp[i + 1][j], piles[j] + dp[i][j - 1])
                else:
                    # second player: lee
                    dp[i][j] = min(-piles[i] + dp[i + 1][j], -piles[j] + dp[i][j - 1])
        return dp[0][N - 1] > 0