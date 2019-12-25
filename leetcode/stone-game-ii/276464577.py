# title: stone-game-ii
# detail: https://leetcode.com/submissions/detail/276464577/
# datetime: Wed Nov  6 16:16:13 2019
# runtime: 560 ms
# memory: 13.1 MB

from functools import lru_cache

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        self.cache = {}
        r = self._play2(piles)
        return r
    
    def _play1(self, piles):
        MAX = sum(piles)
        
        @lru_cache(None)
        def _dfs(start, m, player):
            if start >= len(piles):
                return 0
            next_player = (player + 1) % 2
            _max = 0
            _min = MAX
            for x in range(1, 2 * m + 1):
                if start + x > len(piles):
                    break
                s = _dfs(start + x, max(x, m), next_player)
                
                if player == 0:
                    s += sum(piles[start: start + x])
                    if s > _max:
                        _max = s
                else:
                    if s < _min:
                        _min = s
            if player == 0:
                return _max
            # print(player, _min)
            return _min
        
        return _dfs(0, 1, 0)
    
    def _play2(self, piles):
        N = len(piles)
        MAX = sum(piles)
        M = N // 2 + 1
        dp = [[[0 for _ in range(2)] for _ in range(M)] for _ in range(N + 1)]

        
        for i in reversed(range(N)):
            for m in range(1, M):
                min_ = MAX
                max_ = 0
                for x in range(1, 2 * m + 1):
                    if i + x > N:
                        break
                    
                    v1 = dp[i + x][min(max(x, m), M - 1)][0]
                    v2 = dp[i + x][min(max(x, m), M - 1)][1] + sum(piles[i:i + x])
                    if v1 < min_:
                        min_ = v1
                    if v2 > max_:
                        max_= v2
                dp[i][m][0] = max_
                dp[i][m][1] = min_
        
        return dp[0][1][0]
