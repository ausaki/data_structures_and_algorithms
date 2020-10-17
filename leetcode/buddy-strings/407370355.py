# title: buddy-strings
# detail: https://leetcode.com/submissions/detail/407370355/
# datetime: Sun Oct 11 22:43:15 2020
# runtime: 28 ms
# memory: 14.3 MB

class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        m, n = len(A), len(B)
        if m != n or m < 2:
            return False
        idx = []
        for i in range(m):
            if A[i] != B[i]:
                idx.append(i)
                if len(idx) > 2:
                    return False
        if len(idx) == 1:
            return False
        if len(idx) == 0:
            return len(set(A)) < m
        return A[idx[1]] == B[idx[0]] and A[idx[0]] == B[idx[1]]
            