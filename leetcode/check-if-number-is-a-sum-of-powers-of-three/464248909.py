# title: check-if-number-is-a-sum-of-powers-of-three
# detail: https://leetcode.com/submissions/detail/464248909/
# datetime: Sat Mar  6 22:44:42 2021
# runtime: 2164 ms
# memory: 630.7 MB

class Solution:
    powers = [1] * 16
    for i in range(1, 16):
        powers[i] = powers[i - 1] * 3
        
    def checkPowersOfThree(self, n: int) -> bool:
        @lru_cache(None)
        def check(n, i):
            if n == 0:
                return True
            if n < 0:
                return False
            if i >= 16:
                return False
            return check(n - self.powers[i], i + 1) or check(n, i + 1)
        
        return check(n, 0)