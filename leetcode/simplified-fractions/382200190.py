# title: simplified-fractions
# detail: https://leetcode.com/submissions/detail/382200190/
# datetime: Mon Aug 17 20:52:25 2020
# runtime: 188 ms
# memory: 14 MB

class Solution:
    # @lru_cache(None)
    def simplifiedFractions(self, n: int) -> List[str]:
        result = []
        for i in range(2, n + 1):
            for j in range(1, i):
                if math.gcd(i, j) == 1:
                    result.append('{}/{}'.format(j, i))
        return result