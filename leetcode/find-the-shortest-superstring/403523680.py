# title: find-the-shortest-superstring
# detail: https://leetcode.com/submissions/detail/403523680/
# datetime: Fri Oct  2 21:35:30 2020
# runtime: 712 ms
# memory: 52.8 MB

class Solution:
    def shortestSuperstring(self, A: List[str]) -> str:
        @lru_cache(None)
        def dp(p, mask):
            if mask == 0:
                return 0, 0
            result = 0
            k = -1
            for j in range(n):
                if not (mask >> j) & 1:
                    continue
                l = g[p].get(j, 0)
                h, x = dp(j,  mask & ~(1 << j))
                h += l
                if h >= result:
                    result = h
                    k = j
            return result, k
        A.insert(0, '*')
        n = len(A)
        g = collections.defaultdict(dict)
        for i in range(n):
            for j in range(n):
                if i == j: continue
                h = min(len(A[i]), len(A[j]))
                for l in range(h - 1, 0, -1):
                    if A[i][-l:] == A[j][:l]:
                        g[i][j] = l
                        break
        mask = (1 << n) - 2
        p = 0
        result = ''
        for i in range(1, n):
            l, x = dp(p, mask)
            result += A[x][g[p].get(x, 0):]
            p = x
            mask = mask & ~(1 << x)
        return result
        