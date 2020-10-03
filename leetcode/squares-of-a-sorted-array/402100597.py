# title: squares-of-a-sorted-array
# detail: https://leetcode.com/submissions/detail/402100597/
# datetime: Tue Sep 29 12:29:32 2020
# runtime: 204 ms
# memory: 15.4 MB

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        for i, a in enumerate(A):
            A[i] = a * a
        A.sort()
        return A