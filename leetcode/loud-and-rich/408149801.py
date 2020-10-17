# title: loud-and-rich
# detail: https://leetcode.com/submissions/detail/408149801/
# datetime: Tue Oct 13 15:25:06 2020
# runtime: 424 ms
# memory: 23.5 MB

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        g = collections.defaultdict(list)
        for x, y in richer:
            g[y].append(x)
        
        @lru_cache(None)
        def find(x):
            return min(itertools.chain((find(y) for y in g[x]), [x]), key=quiet.__getitem__)
        
        return [find(x) for x in range(len(quiet))]