# title: rotate-string
# detail: https://leetcode.com/submissions/detail/411781526/
# datetime: Thu Oct 22 14:54:41 2020
# runtime: 28 ms
# memory: 14.1 MB

class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        return A == B or any(A[i:] + A[:i] == B for i in range(len(A)))
