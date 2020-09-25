# title: longest-well-performing-interval
# detail: https://leetcode.com/submissions/detail/397098560/
# datetime: Fri Sep 18 00:54:56 2020
# runtime: 236 ms
# memory: 14.4 MB

class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        curr_sum = 0
        prev_sum = {}
        res = 0
        for i, h in enumerate(hours):
            curr_sum += 1 if h > 8 else -1
            if curr_sum > 0:
                res = i + 1
            else:
                res = max(res, i - prev_sum.get(curr_sum - 1, i))
            prev_sum.setdefault(curr_sum, i)
        return res