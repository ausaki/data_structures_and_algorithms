# title: smallest-string-with-swaps
# detail: https://leetcode.com/submissions/detail/395594915/
# datetime: Mon Sep 14 21:37:20 2020
# runtime: 708 ms
# memory: 50.5 MB

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        parents = [i for i in range(len(s))]
        ranks = [1 for _ in range(len(s))]
        components = collections.defaultdict(list)
        def find(x):
            while x != parents[x]:
                parents[x] = parents[parents[x]]
                x = parents[x]
            return x
        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False
            if ranks[px] > ranks[py]:
                parents[py] = px
            elif ranks[px] < ranks[py]:
                parents[px] = py
            else:
                parents[py] = px
                ranks[px] += 1
            return True
        for a, b in pairs:
            union(a, b)
        for i in range(len(parents)):
            components[find(i)].append(s[i])
        for comp_id in components:
            components[comp_id].sort(reverse=True)
        res = ''
        for i in range(len(s)):
            res += components[find(i)].pop()
        return res