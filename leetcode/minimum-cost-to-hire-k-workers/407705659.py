# title: minimum-cost-to-hire-k-workers
# detail: https://leetcode.com/submissions/detail/407705659/
# datetime: Mon Oct 12 15:58:40 2020
# runtime: 184 ms
# memory: 16 MB

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        n = len(quality)
        if K == 1:
            return min(wage)
        ratio = [w / q for q, w in zip(quality, wage)]
        idx = sorted(range(n), key=ratio.__getitem__)
        q = []
        s = 0
        result = math.inf
        for i in range(K - 1):
            heapq.heappush(q, -quality[idx[i]])
            s += quality[idx[i]]
        for i in range(K - 1, n):
            qa = quality[idx[i]]
            result = min(result, (s + qa) * ratio[idx[i]])
            if -qa > q[0]:
                s += heapq.heappushpop(q, -qa) + qa
        return result
