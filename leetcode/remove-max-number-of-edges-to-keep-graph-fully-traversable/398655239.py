# title: remove-max-number-of-edges-to-keep-graph-fully-traversable
# detail: https://leetcode.com/submissions/detail/398655239/
# datetime: Mon Sep 21 15:23:02 2020
# runtime: 2144 ms
# memory: 52.8 MB

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
                return False
            if elements[i] <= elements[j]:
                if elements[i] == elements[j]:
                    elements[i] -= 1
                elements[j] = i
            else:
                elements[i] = j
            return True
        
        def count(elements):
            return sum(1 for i in elements if i < 0)
        
        result = 0
        for t, u, v in edges:
            if t != 3:
                continue
            if not union(elements, u, v):
                result += 1
        elements2 = elements[:]
        for t, u, v in edges:
            if t == 1:
                if not union(elements, u, v):
                    result += 1
            elif t == 2:
                if not union(elements2, u, v):
                    result += 1
        if count(elements) > 1 or count(elements2) > 1:
            return -1
        return result