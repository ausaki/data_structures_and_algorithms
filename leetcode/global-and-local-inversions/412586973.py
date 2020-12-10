# title: global-and-local-inversions
# detail: https://leetcode.com/submissions/detail/412586973/
# datetime: Sat Oct 24 21:36:57 2020
# runtime: 408 ms
# memory: 14.8 MB

class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        n = len(A)
        i = 0
        while i < n:
            if i == A[i]:
                i += 1
                continue
            if i + 1 < n and i + 1 == A[i] and A[i + 1] == i:
                i += 2
                continue
            return False
        return True