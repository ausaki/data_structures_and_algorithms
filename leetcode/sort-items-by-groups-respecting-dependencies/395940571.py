# title: sort-items-by-groups-respecting-dependencies
# detail: https://leetcode.com/submissions/detail/395940571/
# datetime: Tue Sep 15 13:24:07 2020
# runtime: 468 ms
# memory: 29.1 MB

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
        g2 = collections.defaultdict(list)
        indeg2 = collections.Counter()
        for i in range(n):
            for j in beforeItems[i]:
                if group[i] == group[j]:
                    g2[i].append(j)
                    indeg2[j] += 1
                else:
                    g1[group[i]].append(group[j])
                    indeg1[group[j]] += 1
        sorted_groups = toposort(groups.keys(), g1, indeg1)
        if not sorted_groups:
            return []
        result = []
        for g in sorted_groups:
            g_ = toposort(groups[g], g2, indeg2)
            if not g_:
                return []
            result += g_
        return reversed(result)
        
        
        