# title: smallest-rotation-with-highest-score
# detail: https://leetcode.com/submissions/detail/411832178/
# datetime: Thu Oct 22 18:04:18 2020
# runtime: 208 ms
# memory: 16.6 MB

class Solution:
    def bestRotation(self, A: List[int]) -> int:
        n = len(A)
        q = [0] * (n + 1)
        curr_score = 0
        for i in range(n):
            if A[i] <= i:
                q[min(n, i - A[i] + 1)] += 1
                curr_score += 1
        max_score = curr_score
        k = 0
        for i in range(1, n):
            curr_score -= q[i]
            if A[i - 1] <= n - 1:
                curr_score += 1
                q[min(n, i + n - 1 - A[i - 1] + 1)] += 1
            if curr_score > max_score:
                max_score = curr_score
                k = i
        return k