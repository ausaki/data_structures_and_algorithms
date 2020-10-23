# title: bus-routes
# detail: https://leetcode.com/submissions/detail/411001709/
# datetime: Tue Oct 20 16:54:34 2020
# runtime: 552 ms
# memory: 23.1 MB

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0
        n = len(routes)
        routes = [set(rt) for rt in routes]
        g = collections.defaultdict(list)
        for i, j in itertools.combinations(range(n), 2):
            if routes[i] & routes[j]:
                g[i].append(j)
                g[j].append(i)
        
        q = collections.deque()
        visited = [0] * n
        end = [0] * n
        for i, rt in enumerate(routes):
            if S in rt:
                q.append(i)
                visited[i] = 1
            if T in rt:
                end[i] = 1
        if any(end[i] for i in q):
            return 1
        steps = 1
        while q:
            for _ in range(len(q)):
                i = q.popleft()
                for j in g[i]:
                    if end[j]:
                        return steps + 1
                    if not visited[j]:
                        visited[j] = 1
                        q.append(j)
            steps += 1
        return -1