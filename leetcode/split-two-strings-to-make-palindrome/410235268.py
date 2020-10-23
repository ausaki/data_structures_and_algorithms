# title: split-two-strings-to-make-palindrome
# detail: https://leetcode.com/submissions/detail/410235268/
# datetime: Sun Oct 18 21:19:46 2020
# runtime: 116 ms
# memory: 15.2 MB

class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        n = len(a)
        if n == 1:
            return True
        def check(a, b, i, j):
            while i < j and a[i] == b[j]:
                i += 1
                j -= 1
            return i, j
        for a, b in [(a, a), (b, b), (a, b), (b, a), ]:
            i, j = 0, n - 1
            i, j = check(a, b, i, j)
            if i >= j:
                return True
            ii, jj = i, j
            i, j = check(b, b, i, j)
            if i >= j:
                return True
            i, j = check(a, a, ii, jj)
            if i >= j:
                return True
        return False