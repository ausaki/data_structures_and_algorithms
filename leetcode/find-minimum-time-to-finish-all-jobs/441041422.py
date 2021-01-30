# title: find-minimum-time-to-finish-all-jobs
# detail: https://leetcode.com/submissions/detail/441041422/
# datetime: Sun Jan 10 15:06:46 2021
# runtime: 192 ms
# memory: 14.4 MB

class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        def assign(i):
            if i == n:
                return max(w)
            res = 10 ** 9
            for j in range(k):
                w[j] += jobs[i]
                res = min(res, assign(i + 1))
                w[j] -= jobs[i]
            return res
        
        n = len(jobs)
        jobs.sort(reverse=True)
        w = jobs[:k]
        res = assign(k)
        return res