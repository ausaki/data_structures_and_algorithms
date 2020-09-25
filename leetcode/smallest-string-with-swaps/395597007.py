# title: smallest-string-with-swaps
# detail: https://leetcode.com/submissions/detail/395597007/
# datetime: Mon Sep 14 21:43:18 2020
# runtime: 732 ms
# memory: 50.5 MB

class DisjSet:
    def __init__(self, n):
        self.disj_set = [-1] * n
        
    def find(self, x):
        while self.disj_set[x] >= 0:
            x = self.disj_set[x]
        return x
    
    def union(self, x, y):
        i = self.find(x)
        j = self.find(y)
        if i == j:
            return
        if self.disj_set[i] < self.disj_set[j]:
            self.disj_set[j] = i
        else:
            if self.disj_set[i] == self.disj_set[j]:
                self.disj_set[j] -= 1
            self.disj_set[i] = j

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        parents = [i for i in range(len(s))]
        ranks = [1 for _ in range(len(s))]
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
        g = collections.defaultdict(collections.Counter)
        for i in range(n):
            g[find(i)][s[i]] += 1
        for i in g:
            g[i] = [[k, v] for k, v in g[i].items()]
            g[i].sort(reverse=True)
        result = []
        for i in range(n):
            j = find(i)
            chars = g[j]
            result.append(chars[-1][0])
            chars[-1][1] -= 1
            if chars[-1][1] == 0:
                chars.pop()
        return ''.join(result)