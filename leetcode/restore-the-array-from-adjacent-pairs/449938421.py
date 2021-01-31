# title: restore-the-array-from-adjacent-pairs
# detail: https://leetcode.com/submissions/detail/449938421/
# datetime: Sun Jan 31 10:55:40 2021
# runtime: 1560 ms
# memory: 63.2 MB

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        g = collections.defaultdict(list)
        d = set()
        for a, b in adjacentPairs:
            g[a].append(b)
            g[b].append(a)
            if len(g[a]) == 1:
                d.add(a)
            else:
                d.remove(a)
            if len(g[b]) == 1:
                d.add(b)
            else:
                d.remove(b)
        curr = d.pop()
        res = [curr]
        prev, curr = curr, g[curr][0]
        for i in range(len(g) - 1):
            res.append(curr)
            if len(g[curr]) == 2:
                a, b = g[curr]
                prev, curr = curr, (a if a != prev else b)
        return res