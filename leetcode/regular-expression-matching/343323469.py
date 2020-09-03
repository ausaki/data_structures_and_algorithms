# title: regular-expression-matching
# detail: https://leetcode.com/submissions/detail/343323469/
# datetime: Sat May 23 11:10:35 2020
# runtime: 1140 ms
# memory: 13.8 MB

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        N = len(s)
        M = len(p)
        def match(i, j):
            # print(i, j)
            if j == M:
                return i == N
            if i == N:
                return j + 1 < M and p[j + 1] == '*' and match(i, j + 2)
            if j + 1 >= M or p[j + 1] != '*':
                return (s[i] == p[j] or p[j] == '.') and match(i + 1, j + 1)
            if s[i] == p[j] or p[j] == '.':
                if match(i + 1, j):
                    return True
            return match(i, j + 2)
        
        return match(0, 0)