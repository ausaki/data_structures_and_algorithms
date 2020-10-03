# title: maximum-width-ramp
# detail: https://leetcode.com/submissions/detail/402633045/
# datetime: Wed Sep 30 17:40:38 2020
# runtime: 356 ms
# memory: 20.7 MB

class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        n = len(A)
        candidates = [(A[n - 1], n - 1)]
        result = 0
        for i in range(n - 2, -1, -1):
            j = bisect.bisect(candidates, (A[i], ))
            if j == len(candidates):
                candidates.append((A[i], i))
            else:
                result = max(result, candidates[j][1] - i)
        return result