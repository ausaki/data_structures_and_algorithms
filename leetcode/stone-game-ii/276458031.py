# title: stone-game-ii
# detail: https://leetcode.com/submissions/detail/276458031/
# datetime: Wed Nov  6 15:42:19 2019
# runtime: 160 ms
# memory: 13.7 MB

from functools import lru_cache

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        self.cache = {}
        r = self._play1(piles)
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
        dp = [[[0 for _ in range(2)] for _ in range(N)] for _ in range(N)]
        MIN = sum(piles)
        for i in range(N):
            for m in range(1, N):
                min_ = MIN
                max_ = 0
                for x in range(1, 2 * m + 1):
                    v = sum(piles[i:i + x]) + dp[i + x][m][1]
                    if v > max_:
                        max_= v
                dp[i][m][0] = max_
    
    def _play3(self, piles):
        @lru_cache(None)
        def dfs(p, m, f):
            if p >= len(piles):
                return 0
            
            if f == 'L':
			    # Lee tries to minimize the piles Alex can get
                return min([dfs(p + i, max(m, i), 'A') for i in range(1, 2*m + 1)])
            else:
			    # Alex tries to maximize the piles Alex can get
                return max(sum(piles[p:p + i]) + dfs(p+i, max(m, i), 'L') for i in range(1, 2*m+1))
                
        return dfs(0, 1, 'A')