# title: course-schedule-ii
# detail: https://leetcode.com/submissions/detail/284326237/
# datetime: Sat Dec  7 22:57:34 2019
# runtime: 104 ms
# memory: 14.3 MB

from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegrees = {i: 0 for i in range(numCourses)}
        res = []
        for edge in prerequisites:
            graph[edge[1]].append(edge[0])
            indegrees[edge[0]] += 1
        # find all V with in-degree equals to 0
        deg0 = deque([i for i, deg in indegrees.items() if deg == 0])
        while deg0:
            i = deg0.popleft()
            indegrees.pop(i)
            res.append(i)
            for j in graph[i]:
                indegrees[j] -= 1
                if indegrees[j] == 0:
                    deg0.append(j)
        return res if not indegrees else []