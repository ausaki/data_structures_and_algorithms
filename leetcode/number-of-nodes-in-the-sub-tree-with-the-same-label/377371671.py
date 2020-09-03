# title: number-of-nodes-in-the-sub-tree-with-the-same-label
# detail: https://leetcode.com/submissions/detail/377371671/
# datetime: Fri Aug  7 16:50:03 2020
# runtime: 2244 ms
# memory: 194.7 MB

import collections
from functools import lru_cache
import sys

class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        # print(sys.getrecursionlimit())
        tree = collections.defaultdict(list)
        for v1, v2 in edges:
            tree[v1].append(v2)
            tree[v2].append(v1)
        queue = collections.deque([0])
        while queue:
            node = queue.popleft()
            neighbors = tree[node]
            for nb in neighbors:
                tree[nb].remove(node)
                queue.append(nb)

        result = [1] * n
        
        def dfs(node):
            if node not in tree:
                return collections.Counter({labels[node]: 1})
            children = tree.get(node)
            cnt = collections.Counter()
            for child in children:
                cnt.update(dfs(child))
            cnt[labels[node]] += 1
            result[node] = cnt[labels[node]]
            return cnt
        dfs(0)
        return result
                