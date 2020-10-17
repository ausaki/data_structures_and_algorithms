# title: fruit-into-baskets
# detail: https://leetcode.com/submissions/detail/405159106/
# datetime: Tue Oct  6 14:30:23 2020
# runtime: 752 ms
# memory: 20.2 MB

class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        g = [[tree[0], 0]]
        for t in tree:
            if t == g[-1][0]:
                g[-1][1] += 1
            else:
                g.append([t, 1])
        n = len(g)
        if n <= 2:
            return sum(cnt for _, cnt in g)
        a, b = g[0][0], g[1][0]
        total = g[0][1] + g[1][1]
        result = total
        for i in range(2, n):
            t, cnt = g[i]
            if t == a or t == b:
                total += cnt
            else:
                a, b = g[i - 1][0], t
                total = g[i - 1][1] + cnt
            result = max(result, total)
        return result
        