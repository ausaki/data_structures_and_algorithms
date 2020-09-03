# title: parallel-courses-ii
# detail: https://leetcode.com/submissions/detail/379886231/
# datetime: Wed Aug 12 22:23:04 2020
# runtime: 3868 ms
# memory: 13.9 MB

class Solution:
    def minNumberOfSemesters(self, n: int, dependencies: List[List[int]], k: int) -> int:
        graph = collections.defaultdict(set)
        in_degrees = {i: 0 for i in range(1, n + 1)}
        for c1, c2 in dependencies:
            graph[c1].add(c2)
            in_degrees[c2] += 1
        
        def plan():
            result = n
            if not in_degrees:
                return 0
            in0 = [c for c, d in in_degrees.items() if d == 0]
            if len(in0) == len(in_degrees):
                return (len(in0) + k - 1) // k
            combs = itertools.combinations(in0, k) if k < len(in0) else [in0]
            for nodes in combs:
                # print(nodes)
                for node in nodes:
                    in_degrees.pop(node)
                    for nb in graph[node]:
                        in_degrees[nb] -= 1
                result = min(result, plan())
                for node in nodes:
                    in_degrees[node] = 0
                    for nb in graph[node]:
                        in_degrees[nb] += 1
            # print(result + 1)
            return result + 1
        
        return plan()
                
        