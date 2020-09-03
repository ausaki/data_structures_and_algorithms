# title: probability-of-a-two-boxes-having-the-same-number-of-distinct-balls
# detail: https://leetcode.com/submissions/detail/381661733/
# datetime: Sun Aug 16 17:22:37 2020
# runtime: 48 ms
# memory: 15.5 MB

class Solution:
    def getProbability(self, balls: List[int]) -> float:
        @lru_cache(None)
        def C(n, m):
            if m > n // 2:
                return C(n, n - m)
            return math.factorial(n) / math.factorial(m) / math.factorial(n - m)
        
        @lru_cache(None)
        def choose(i, k, d1, d2, cnt):
            if k == 0 and i <= n:
                return cnt, (cnt if d1 == d2 + n - i else 0)
            if k < 0 or i == n:
                return 0, 0
            total = 0
            equal = 0
            for j in range(balls[i] + 1):
                if k - j < 0:
                    break
                t, e = choose(i + 1, k - j, d1 + (1 if j > 0 else 0), d2 + (1 if j < balls[i] else 0), cnt * C(balls[i], j))
                total += t
                equal += e
            return total, equal
        
        n = len(balls)
        k = sum(balls)
        t, e = choose(0, k // 2, 0, 0, 1)
        return e / t
            
                