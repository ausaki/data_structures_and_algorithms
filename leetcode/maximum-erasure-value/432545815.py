# title: maximum-erasure-value
# detail: https://leetcode.com/submissions/detail/432545815/
# datetime: Sun Dec 20 15:42:01 2020
# runtime: 1332 ms
# memory: 28.2 MB

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        pos = {}
        prefix = [0]
        l = -1
        res = 0
        for i, j in enumerate(nums):
            prefix.append(prefix[-1] + j)
            l = max(l, pos.get(j, -1) + 1)
            res = max(res, prefix[i + 1] - prefix[l])
            pos[j] = i
        return res