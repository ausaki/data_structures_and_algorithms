# title: global-and-local-inversions
# detail: https://leetcode.com/submissions/detail/412586721/
# datetime: Sat Oct 24 21:35:49 2020
# runtime: 356 ms
# memory: 19.6 MB

class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        def check(i):
            if i == n:
                return True
            if i == A[i]:
                return check(i + 1)
            if i + 1 < n and i + 1 == A[i] and A[i + 1] == i:
                return check(i + 2)
            return False
        
        n = len(A)
        return check(0)