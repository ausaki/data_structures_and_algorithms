# title: rotate-string
# detail: https://leetcode.com/submissions/detail/411782042/
# datetime: Thu Oct 22 14:56:17 2020
# runtime: 24 ms
# memory: 14.1 MB

class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        return len(A) == len(B) and (A == B or any(A[i:] + A[:i] == B for i in range(len(A))))
