# title: sort-items-by-groups-respecting-dependencies
# detail: https://leetcode.com/submissions/detail/395950016/
# datetime: Tue Sep 15 13:46:43 2020
# runtime: 512 ms
# memory: 26.5 MB

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        def toposort(V, g, indeg):
            result = []
            q = collections.deque([v for v in V if indeg[v] == 0])
            while q:
                v = q.popleft()
                result.append(v)
                for w in g[v]:
                    indeg[w] -= 1
                    if indeg[w] == 0:
                        q.append(w)
            return result if len(result) == len(V) else []
        
        groups = collections.defaultdict(list)
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1
            groups[group[i]].append(i)
        g1 = collections.defaultdict(list)
        indeg1 = collections.Counter()
        indeg2 = [0] * n
        for i in range(n):
            for j in beforeItems[i]:
                indeg2[j] += 1
                if group[i] != group[j]:
                    g1[group[i]].append(group[j])
                    indeg1[group[j]] += 1
        rank = [0] * n
        r = 0
        q = collections.deque([i for i, v in enumerate(indeg2) if v == 0])
        while q:
            v = q.popleft()
            rank[v] = r
            r += 1
            for w in beforeItems[v]:
                indeg2[w] -= 1
                if indeg2[w] == 0:
                    q.append(w)
        if r != n:
            return []
        sorted_groups = toposort(groups.keys(), g1, indeg1)
        if not sorted_groups:
            return []
        result = []
        for g in sorted_groups:
            groups[g].sort(key=rank.__getitem__)
            result += groups[g]
        return reversed(result)
        
        
        