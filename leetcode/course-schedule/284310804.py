# title: course-schedule
# detail: https://leetcode.com/submissions/detail/284310804/
# datetime: Sat Dec  7 20:27:10 2019
# runtime: 200 ms
# memory: 13.9 MB

from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegrees = {i: 0 for i in range(numCourses)}
        for edge in prerequisites:
            graph[edge[1]].append(edge[0])
            indegrees[edge[0]] += 1
        while True:
            # find all V with in-degree equals to 0
            deg0 = [i for i, deg in indegrees.items() if deg == 0]
            if not deg0:
                return not indegrees
            for i in deg0:
                indegrees.pop(i)
                for j in graph[i]:
                    indegrees[j] -= 1
