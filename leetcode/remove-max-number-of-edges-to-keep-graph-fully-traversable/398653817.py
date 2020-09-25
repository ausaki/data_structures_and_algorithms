# title: remove-max-number-of-edges-to-keep-graph-fully-traversable
# detail: https://leetcode.com/submissions/detail/398653817/
# datetime: Mon Sep 21 15:18:24 2020
# runtime: 2188 ms
# memory: 53.5 MB

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        elements = [-1] * (n + 1)
        elements[0] = 0
        def find(elements, i):
            while elements[i] >= 0:
                i = elements[i]
            return i
        
        def union(elements, i, j):
            i = find(elements, i)
            j = find(elements, j)
            if i == j:
                return
            if elements[i] <= elements[j]:
                if elements[i] == elements[j]:
                    elements[i] -= 1
                elements[j] = i
            else:
                elements[i] = j
        
        def count(elements):
            return sum(1 for i in elements if i < 0)
        
        result = 0
        for t, u, v  in edges:
            if t != 3:
                continue
            if find(elements, u) == find(elements, v):
                result += 1
            else:
                union(elements, u, v)
        elements2 = elements[:]
        for t, u, v in edges:
            if t == 1:
                if find(elements, u) == find(elements, v):
                    result += 1
                else:
                    union(elements, u, v)
            elif t == 2:
                if find(elements2, u) == find(elements2, v):
                    result += 1
                else:
                    union(elements2, u, v)
        if count(elements) > 1 or count(elements2) > 1:
            return -1
        return result