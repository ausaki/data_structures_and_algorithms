# title: smallest-string-with-swaps
# detail: https://leetcode.com/submissions/detail/395586916/
# datetime: Mon Sep 14 21:12:06 2020
# runtime: 1296 ms
# memory: 51.7 MB

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        g = collections.defaultdict(list)
        for a, b in pairs:
            g[a].append(b)
            g[b].append(a)
        n = len(s)
        s = list(s)
        while g:
            i, j = g.popitem()
            visited = {i}
            visited.update(j)
            chars = collections.Counter()
            q = collections.deque(j)
            while q:
                i = q.popleft()
                if i in g:
                    j = g.pop(i)
                    q.extend(j)
                    visited.update(j)
            visited = sorted(visited)
            for i in visited:
                chars[s[i]] += 1
            j = 0
            for c in sorted(chars):
                for k in range(chars[c]):
                    s[visited[j]] =  c
                    j += 1
        return ''.join(s)