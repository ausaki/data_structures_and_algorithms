# title: global-and-local-inversions
# detail: https://leetcode.com/submissions/detail/288946475/
# datetime: Fri Dec 27 19:35:50 2019
# runtime: 356 ms
# memory: 13.3 MB

class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        N = len(A)
        i = 0
        while i < N:
            if A[i] == i:
                i += 1
                continue
            if A[i] == i + 1 and A[i + 1] == i:
                i += 2
                continue
            return False
        return True
            