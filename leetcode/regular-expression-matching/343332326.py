# title: regular-expression-matching
# detail: https://leetcode.com/submissions/detail/343332326/
# datetime: Sat May 23 11:42:13 2020
# runtime: 1152 ms
# memory: 14 MB

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # s += '#'
        # p += '#'
        N = len(s)
        M = len(p)
        def match(i, j):
            # print(i, j)
            if j == M:
                return i == N
            if i == N:
                while j + 1 < M and p[j + 1] == '*':
                    j += 2
                return j == M
            if j + 1 >= M or p[j + 1] != '*':
                return (s[i] == p[j] or p[j] == '.') and match(i + 1, j + 1)
            if s[i] == p[j] or p[j] == '.':
                if match(i + 1, j):
                    return True
            return match(i, j + 2)
        
        return match(0, 0)