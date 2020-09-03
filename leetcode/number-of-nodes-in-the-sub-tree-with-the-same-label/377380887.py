# title: number-of-nodes-in-the-sub-tree-with-the-same-label
# detail: https://leetcode.com/submissions/detail/377380887/
# datetime: Fri Aug  7 17:24:35 2020
# runtime: 2028 ms
# memory: 183.4 MB

import collections
from functools import lru_cache
import sys

class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        tree = collections.defaultdict(set)
        for v1, v2 in edges:
            tree[v1].add(v2)
            tree[v2].add(v1)
        result = [1] * n
        # cnt = 
        def dfs(node):
            children = tree[node]
            if len(children) == 0:
                return collections.Counter({labels[node]: 1})
            cnt = None
            for child in children:
                tree[child].remove(node)
                if cnt is None:
                    cnt = dfs(child)
                else:
                    cnt.update(dfs(child))
            cnt[labels[node]] += 1
            result[node] = cnt[labels[node]]
            return cnt
        dfs(0)
        return result
                