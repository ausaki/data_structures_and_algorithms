# title: number-of-nodes-in-the-sub-tree-with-the-same-label
# detail: https://leetcode.com/submissions/detail/377381255/
# datetime: Fri Aug  7 17:26:06 2020
# runtime: 1924 ms
# memory: 169 MB

import collections
from functools import lru_cache
import sys

class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        tree = collections.defaultdict(list)
        for v1, v2 in edges:
            tree[v1].append(v2)
            tree[v2].append(v1)
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
                