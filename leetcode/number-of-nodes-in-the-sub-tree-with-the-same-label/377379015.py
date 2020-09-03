# title: number-of-nodes-in-the-sub-tree-with-the-same-label
# detail: https://leetcode.com/submissions/detail/377379015/
# datetime: Fri Aug  7 17:17:27 2020
# runtime: 1852 ms
# memory: 164.8 MB

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
        # queue = collections.deque([0])
#         while queue:
#             node = queue.popleft()
            
#                 queue.append(nb)

        result = [1] * n
        
        def dfs(node):
            children = tree[node]
            if len(children) == 0:
                return collections.Counter({labels[node]: 1})
            tree[children[0]].remove(node)
            cnt = dfs(children[0])
            for i in range(1, len(children)):
                tree[children[i]].remove(node)
                cnt.update(dfs(children[i]))
            cnt[labels[node]] += 1
            result[node] = cnt[labels[node]]
            return cnt
        dfs(0)
        return result
                