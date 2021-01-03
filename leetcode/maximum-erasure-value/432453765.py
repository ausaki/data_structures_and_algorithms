# title: maximum-erasure-value
# detail: https://leetcode.com/submissions/detail/432453765/
# datetime: Sun Dec 20 10:54:01 2020
# runtime: 1604 ms
# memory: 27.6 MB

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        pos = {}
        prefix = [0]
        l = -1
        res = 0
        for i, j in enumerate(nums):
            prefix.append(prefix[-1] + j)
            p = pos.get(j, -1)
            if p >= l:
                l = p + 1
                res = max(res, prefix[i + 1] - prefix[l])
            else:
                res = max(res, prefix[i + 1] - prefix[l])
            pos[j] = i
        return res