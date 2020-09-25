# title: smallest-string-with-swaps
# detail: https://leetcode.com/submissions/detail/395594749/
# datetime: Mon Sep 14 21:36:52 2020
# runtime: 1052 ms
# memory: 50.6 MB

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
        s = list(s)
        disj = DisjSet(n)
        for a, b in pairs:
            disj.union(a, b)
        g = collections.defaultdict(collections.Counter)
        for i in range(n):
            g[disj.find(i)][s[i]] += 1
        for i in g:
            g[i] = [[k, v] for k, v in g[i].items()]
            g[i].sort(reverse=True)
        for i in range(n):
            j = disj.find(i)
            chars = g[j]
            s[i] = chars[-1][0]
            chars[-1][1] -= 1
            if chars[-1][1] == 0:
                chars.pop()
        return ''.join(s)