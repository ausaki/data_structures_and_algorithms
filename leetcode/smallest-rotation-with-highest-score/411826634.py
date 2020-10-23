# title: smallest-rotation-with-highest-score
# detail: https://leetcode.com/submissions/detail/411826634/
# datetime: Thu Oct 22 17:36:32 2020
# runtime: 260 ms
# memory: 16.9 MB

class Solution:
    def bestRotation(self, A: List[int]) -> int:
        n = len(A)
        q1 = []
        q2 = []
        for i in range(n):
            if A[i] <= i:
                heapq.heappush(q2, i - A[i])
        score = len(q2)
        k = 0
        for i in range(1, n):
            while q2 and q2[0] < i:
                heapq.heappop(q2)
            while q1 and q1[0] < i:
                heapq.heappop(q1)
            if A[i - 1] <= n - 1:
                heapq.heappush(q1, i + n - 1 - A[i - 1])
            s = len(q1) + len(q2)
            if s > score:
                score = s
                k = i
        return k