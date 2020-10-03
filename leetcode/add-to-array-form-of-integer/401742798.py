# title: add-to-array-form-of-integer
# detail: https://leetcode.com/submissions/detail/401742798/
# datetime: Mon Sep 28 16:24:27 2020
# runtime: 264 ms
# memory: 15 MB

class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        A.reverse()
        s = 0
        for i, a in enumerate(A):
            K, b = divmod(K, 10)
            s, a = divmod(a + b + s, 10)
            A[i] = a
            if s == 0 and K == 0:
                break
        K += s
        while K:
            K, b = divmod(K, 10)
            A.append(b)
        return A[::-1]