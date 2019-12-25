# title: elimination-game
# detail: https://leetcode.com/submissions/detail/285273590/
# datetime: Wed Dec 11 23:54:26 2019
# runtime: 32 ms
# memory: 12.7 MB

class Solution:
    def lastRemaining(self, n: int) -> int:
        start, step, l2r = 1, 1, True
        while n > 1:
            if l2r or n % 2:
                start += step
            l2r, step, n = not l2r, step * 2, n // 2
        return start
            