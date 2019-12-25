# title: course-schedule
# detail: https://leetcode.com/submissions/detail/284311825/
# datetime: Sat Dec  7 20:38:24 2019
# runtime: 96 ms
# memory: 13.8 MB

from collections import deque, defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegrees = {i: 0 for i in range(numCourses)}
        for edge in prerequisites:
            graph[edge[1]].append(edge[0])
            indegrees[edge[0]] += 1
        # find all V with in-degree equals to 0
        deg0 = deque([i for i, deg in indegrees.items() if deg == 0])
        while deg0:
            i = deg0.popleft()
            indegrees.pop(i)
            for j in graph[i]:
                indegrees[j] -= 1
                if indegrees[j] == 0:
                    deg0.append(j)
        return not indegrees