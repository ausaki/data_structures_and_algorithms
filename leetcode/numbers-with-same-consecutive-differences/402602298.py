# title: numbers-with-same-consecutive-differences
# detail: https://leetcode.com/submissions/detail/402602298/
# datetime: Wed Sep 30 15:41:50 2020
# runtime: 32 ms
# memory: 15 MB

class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        @lru_cache(None)
        def dfs(i, p):
            if i == n:
                nums.append(p)
                return
            if i == 0:
                for j in range(1, 10):
                    dfs(i + 1, j)
            else:
                d = p % 10
                if d + k < 10:
                    dfs(i + 1, p * 10 + d + k)
                if d - k >= 0:
                    dfs(i + 1, p * 10 + d - k)
        
        nums = []
        dfs(0, 0)
        return nums