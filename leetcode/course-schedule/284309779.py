# title: course-schedule
# detail: https://leetcode.com/submissions/detail/284309779/
# datetime: Sat Dec  7 20:16:07 2019
# runtime: 228 ms
# memory: 13.9 MB

from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(set)
        indegrees = {i: 0 for i in range(numCourses)}
        for edge in prerequisites:
            graph[edge[1]].add(edge[0])
            indegrees[edge[0]] += 1
        while graph:
            # find all V with in-degree equals to 0
            l = len(graph)
            for i, degree in indegrees.items():
                if degree == 0 and i in graph:
                    for j in graph[i]:
                        indegrees[j] -= 1
                    graph[i].clear()
                    graph.pop(i)
            if l == len(graph):
                return False
        return True