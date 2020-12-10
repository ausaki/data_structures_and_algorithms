# title: minimize-deviation-in-array
# detail: https://leetcode.com/submissions/detail/429209300/
# datetime: Thu Dec 10 20:12:04 2020
# runtime: 920 ms
# memory: 32 MB

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        pairs = [[i, 2 * i] if i % 2 else [i // (-i & i), i] for i in nums]
        heapq.heapify(pairs)
        maxv = max(pairs)[0]
        res = maxv - pairs[0][0]
        while pairs[0][0] < pairs[0][1]:
            p = heapq.heappop(pairs)
            p[0] *= 2
            heapq.heappush(pairs, p)
            maxv = max(maxv, p[0])
            res = min(res, maxv - pairs[0][0])
        return res
            