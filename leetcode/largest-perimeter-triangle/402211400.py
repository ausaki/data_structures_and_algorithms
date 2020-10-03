# title: largest-perimeter-triangle
# detail: https://leetcode.com/submissions/detail/402211400/
# datetime: Tue Sep 29 18:32:02 2020
# runtime: 196 ms
# memory: 15.1 MB

class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort()
        for i in range(len(A) - 1, 1, -1):
            s = A[i - 1] + A[i - 2]
            if s > A[i]:
                return s + A[i]
        return 0