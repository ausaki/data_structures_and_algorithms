# title: three-equal-parts
# detail: https://leetcode.com/submissions/detail/404227803/
# datetime: Sun Oct  4 12:16:55 2020
# runtime: 648 ms
# memory: 15.4 MB

class Solution:
    def threeEqualParts(self, A: List[int]) -> List[int]:
        def partial_table(sub):
            m = len(sub)
            table = [0] * m
            table[0] = 0
            for i in range(1, m):
                j = table[i - 1]
                while j >= 0 and sub[i] != sub[j]:
                    j = table[j - 1] if j > 0 else -1
                table[i] = j + 1
            return table
        n = len(A)
        b = 0
        while b < n and A[b] == 0:
            b += 1
        if b == n:
            return [0, n - 1]
        A = A[b:]
        n -= b
        table = partial_table(A)
        t = n - 1
        while t > 0:
            l = table[t]
            if l == 0:
                break
            i, j = l, n - l
            while i < j and A[i] == 0:
                i += 1
            if j - i < l:
                t = l - 1
                continue
            eq = True
            for k in range(l):
                if A[i + k] != A[k]:
                    eq = False
                    break
            if eq:
                for k in range(i + l, j):
                    if A[k] != 0:
                        eq = False
                        break
            if eq:
                return [l - 1 + b, i + l + b]
            t = l - 1
        return [-1, -1]