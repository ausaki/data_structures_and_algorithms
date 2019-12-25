# title: longest-well-performing-interval
# detail: https://leetcode.com/submissions/detail/282659265/
# datetime: Sat Nov 30 18:04:44 2019
# runtime: 224 ms
# memory: 13.2 MB

class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        hours = [1 if h > 8 else -1 for h in hours]
        print(hours)
        curr_sum = 0
        prev_sum = {}
        res = 0
        for i, h in enumerate(hours):
            curr_sum += h
            if curr_sum > 0:
                res = i + 1
            else:
                j = prev_sum.get(curr_sum - 1, i)
                if i - j > res:
                    res = i - j
            prev_sum.setdefault(curr_sum, i)
        return res