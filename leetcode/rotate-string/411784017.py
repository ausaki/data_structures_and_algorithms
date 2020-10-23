# title: rotate-string
# detail: https://leetcode.com/submissions/detail/411784017/
# datetime: Thu Oct 22 15:02:29 2020
# runtime: 32 ms
# memory: 14 MB

class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        def g(A, i):
            for j in range(i, len(A)):
                yield A[j]
            for j in range(i):
                yield A[j]
                
        return len(A) == len(B) and (A == B or any(all(a == b for a, b in zip(g(A, i), B)) for i in range(len(A))))
