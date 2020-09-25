# title: previous-permutation-with-one-swap
# detail: https://leetcode.com/submissions/detail/399684104/
# datetime: Wed Sep 23 22:11:31 2020
# runtime: 232 ms
# memory: 14.9 MB

class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        n = len(A)
        for i in range(n - 2, -1, -1):
            if A[i] > A[i + 1]:
                j = bisect.bisect_left(A, A[i], i + 1, n)
                j -= 1
                while A[j] == A[j - 1]:
                    j -= 1
                A[i], A[j] = A[j], A[i]
                break
        return A
            