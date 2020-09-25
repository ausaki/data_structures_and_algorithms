# title: smallest-string-with-swaps
# detail: https://leetcode.com/submissions/detail/395582750/
# datetime: Mon Sep 14 20:57:42 2020
# runtime: 932 ms
# memory: 75.7 MB

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        g = collections.defaultdict(list)
        for a, b in pairs:
            g[a].append(b)
            g[b].append(a)
        
        def find(i, idx, chars):
            for k in g[i]:
                if not visited[k]:
                    visited[k] = 1
                    idx.append(k)
                    chars[s[k]] += 1
                    find(k, idx, chars)
        n = len(s)
        s = list(s)
        visited = [0] * n
        for i in range(n):
            if visited[i]:
                continue
            visited[i] = 1
            idx = [i]
            chars = collections.Counter()
            chars[s[i]] += 1
            find(i, idx, chars)
            idx.sort()
            j = 0
            for c in sorted(chars):
                for k in range(chars[c]):
                    s[idx[j]] =  c
                    j += 1
        return ''.join(s)