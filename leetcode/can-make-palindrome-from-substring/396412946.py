# title: can-make-palindrome-from-substring
# detail: https://leetcode.com/submissions/detail/396412946/
# datetime: Wed Sep 16 12:27:46 2020
# runtime: 1824 ms
# memory: 60.7 MB

class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        A = [0]
        n = len(s)
        for c in s:
            A.append(A[-1] ^ (1 << (ord(c) - 97)))
        result = []
        for l, r, k in queries:
            a = A[r + 1] ^ A[l]
            c = bin(a).count('1')
            result.append(c // 2 <= k)
        return result