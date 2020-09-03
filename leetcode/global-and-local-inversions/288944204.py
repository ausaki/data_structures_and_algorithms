# title: global-and-local-inversions
# detail: https://leetcode.com/submissions/detail/288944204/
# datetime: Fri Dec 27 19:14:32 2019
# runtime: 384 ms
# memory: 13.1 MB

class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        N = len(A)
        k = -1
        i = 1
        while i < N:
            if A[i] > A[i - 1]:
                k = A[i - 1]
                i += 1
                continue
            if A[i] < k:
                return False
            if i + 1 < N and (A[i] > A[i + 1] or A[i + 1] < A[i - 1]):
                return False
            k = A[i - 1]
            i += 2
        return True