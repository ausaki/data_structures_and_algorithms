# title: maximum-number-of-consecutive-values-you-can-make
# detail: https://leetcode.com/submissions/detail/470210108/
# datetime: Sun Mar 21 00:35:22 2021
# runtime: 704 ms
# memory: 19.3 MB

class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        res = 1
        for c in coins:
            if c > res:
                break
            res += c
        return res