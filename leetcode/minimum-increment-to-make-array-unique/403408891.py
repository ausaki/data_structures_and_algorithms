# title: minimum-increment-to-make-array-unique
# detail: https://leetcode.com/submissions/detail/403408891/
# datetime: Fri Oct  2 14:05:00 2020
# runtime: 316 ms
# memory: 19.2 MB

class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        A.sort()
        result = 0
        for i, a in enumerate(A):
            if i and a <= A[i - 1]:
                result += A[i - 1] + 1 - A[i]
                A[i] = A[i - 1] + 1
        return result
                
        