# title: find-minimum-time-to-finish-all-jobs
# detail: https://leetcode.com/submissions/detail/441062398/
# datetime: Sun Jan 10 16:05:08 2021
# runtime: 68 ms
# memory: 14.2 MB

class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        n = len(jobs)
        jobs.sort(reverse=True)
        q = [0] * k
        for j in reversed(jobs):
            heapq.heappushpop(q, q[0] + j)
        
        # 局部最优解
        res = max(q)
        
        def assign(i):
            nonlocal res
            if i == n:
                res = min(res, max(w))
                return
            for j in range(k):
                if w[j] + jobs[i] <= res:
                    w[j] += jobs[i]
                    assign(i + 1)
                    w[j] -= jobs[i]
        
        w = jobs[:k]
        assign(k)
        return res
        