# title: minimum-adjacent-swaps-for-k-consecutive-ones
# detail: https://leetcode.com/submissions/detail/435049805/
# datetime: Sun Dec 27 14:02:14 2020
# runtime: 1308 ms
# memory: 24.4 MB

class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        idx = [i for i, a in enumerate(nums) if a]
        n = len(idx)
        prefix = [0]
        res = math.inf
        for i in range(n):
            prefix.append(prefix[-1] + idx[i])
        for i in range(len(idx) - k + 1):
            a = prefix[i + k] - prefix[k // 2 + i] - prefix[(k + 1) // 2 + i] + prefix[i]
            # if k % 2:
            #     a = prefix[i + k] - prefix[i + (k + 1) // 2] - (prefix[i + k // 2] - prefix[i])
            # else:
            #     a = prefix[i + k] - prefix[i + k // 2] - (prefix[i + k // 2] - prefix[i]) 
            res = min(res, a - (k * k) // 4)
        return res