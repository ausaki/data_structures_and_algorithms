# title: global-and-local-inversions
# detail: https://leetcode.com/submissions/detail/288943653/
# datetime: Fri Dec 27 19:09:22 2019
# runtime: 388 ms
# memory: 13.4 MB

class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        N = len(A)
        k = -1
        i = 0
        while i < N:
            j = i + 1
            while j < N and A[j] > A[j - 1]:
                k = A[j - 1]
                j += 1
            if j == N:
                break
            i = j
            if A[i] < k:
                return False
            if i + 1 < N and (A[i] > A[i + 1] or A[i + 1] < A[i - 1]):
                return False
            k = A[i - 1]
            i += 1
        return True