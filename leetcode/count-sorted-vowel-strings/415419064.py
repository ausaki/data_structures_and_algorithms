# title: count-sorted-vowel-strings
# detail: https://leetcode.com/submissions/detail/415419064/
# datetime: Sun Nov  1 10:44:26 2020
# runtime: 36 ms
# memory: 14.4 MB

class Solution:
    def countVowelStrings(self, n: int) -> int:
        v = 'aeiou'
        @lru_cache(None)
        def dp(i, j):
            if i == n:
                return 1
            if j == 4:
                return 1
            result = 0
            for j in range(j, 5):
                result += dp(i + 1, j)
            return result
        return dp(0, 0)