# title: elimination-game
# detail: https://leetcode.com/submissions/detail/285273148/
# datetime: Wed Dec 11 23:51:13 2019
# runtime: 40 ms
# memory: 12.7 MB

class Solution:
    def lastRemaining(self, n: int) -> int:
        start = 1
        step = 1
        k = n
        l2r = True
        while k > 1:
            if l2r or k % 2:
                start += step
            l2r = not l2r
            step *= 2
            k //= 2
        return start
            