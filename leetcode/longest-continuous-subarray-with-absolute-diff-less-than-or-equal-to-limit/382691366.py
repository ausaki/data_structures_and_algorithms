# title: longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit
# detail: https://leetcode.com/submissions/detail/382691366/
# datetime: Tue Aug 18 21:09:57 2020
# runtime: 1172 ms
# memory: 36.7 MB

class Solution:
    # def longestSubarray(self, nums: List[int], limit: int) -> int:
    def longestSubarray(self, A, limit):
        maxq, minq = [], []
        res = i = 0
        for j, a in enumerate(A):
            heapq.heappush(maxq, [-a, j])
            heapq.heappush(minq, [a, j])
            while -maxq[0][0] - minq[0][0] > limit:
                i = min(maxq[0][1], minq[0][1]) + 1
                while maxq[0][1] < i: heapq.heappop(maxq)
                while minq[0][1] < i: heapq.heappop(minq)
            res = max(res, j - i + 1)
        return res
            
            