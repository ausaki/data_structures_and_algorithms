# title: loud-and-rich
# detail: https://leetcode.com/submissions/detail/408148696/
# datetime: Tue Oct 13 15:21:25 2020
# runtime: 432 ms
# memory: 23.6 MB

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        g = collections.defaultdict(list)
        for x, y in richer:
            g[y].append(x)
        
        @lru_cache(None)
        def find(x):
            return min(min((find(y) for y in g[x]), default=x, key=quiet.__getitem__), x, key=quiet.__getitem__)
        
        return [find(x) for x in range(len(quiet))]