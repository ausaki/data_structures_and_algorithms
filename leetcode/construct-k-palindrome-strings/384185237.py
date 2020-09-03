# title: construct-k-palindrome-strings
# detail: https://leetcode.com/submissions/detail/384185237/
# datetime: Fri Aug 21 20:54:59 2020
# runtime: 84 ms
# memory: 14.4 MB

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        n = len(s)
        if k == n:
            return True
        if k > n:
            return False
        counter = collections.Counter(s)
        odds = 0
        for v in counter.values():
            if v % 2:
                odds += 1
        return k >= odds
        