# title: find-the-shortest-superstring
# detail: https://leetcode.com/submissions/detail/403513265/
# datetime: Fri Oct  2 20:53:08 2020
# runtime: 4048 ms
# memory: 51.8 MB

class Solution:
    def shortestSuperstring(self, A: List[str]) -> str:
        @lru_cache(None)
        def dp(i, p, mask):
            if i == n:
                return 0, 0
            result = 0
            k = -1
            for j in range(n):
                if not (mask >> j) & 1:
                    continue
                h = min(len(A[p]), len(A[j]))
                for l in range(h - 1, 0, -1):
                    if A[p][ -l:] == A[j][:l]:
                        h, x = dp(i + 1, j, mask & ~(1 << j))
                        h += l
                        if h > result:
                            result = h
                            k = j
                        break
                h, x = dp(i + 1, j, mask & ~(1 << j))
                if h >= result:
                    result = h
                    k = j
            return result, k
        A.insert(0, '*')
        n = len(A)
        mask = (1 << n) - 2
        p = 0
        idx = []
        for i in range(1, n):
            l, x = dp(i, p, mask)
            idx.append([l, x])
            p = x
            mask = mask & ~(1 << x)
        result = ''
        for i, (l, x) in enumerate(idx):
            y = 0
            if i + 1 < len(idx):
                y = idx[i + 1][0]
            result += A[x][l - y:]
        return result
        