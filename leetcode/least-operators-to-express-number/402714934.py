# title: least-operators-to-express-number
# detail: https://leetcode.com/submissions/detail/402714934/
# datetime: Wed Sep 30 23:11:54 2020
# runtime: 36 ms
# memory: 14.4 MB

class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        poly = []
        while target:
            target, r = divmod(target, x)
            poly.append(r)
        poly.append(0)
        n = len(poly)
        @lru_cache(None)
        def dfs(i, d):
            if i == n:
                return -1
            if poly[i] == 0:
                return dfs(i + 1, poly[i + 1] if i + 1 < n else 0)
            j = (i if i else 2) * poly[i]
            a = j + dfs(i + 1, poly[i + 1] if i + 1 < n else 0) 
            b = 10 ** 9
            if i + 1 < n:
                poly[i + 1] += 1
                j = (i if i else 2) * (x - poly[i])
                b = j + dfs(i + 1, poly[i + 1])
                poly[i + 1] -= 1
            return min(a, b)
        result = dfs(0, poly[1])
        return result
        