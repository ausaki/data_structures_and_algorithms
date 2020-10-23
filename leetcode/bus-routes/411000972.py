# title: bus-routes
# detail: https://leetcode.com/submissions/detail/411000972/
# datetime: Tue Oct 20 16:51:26 2020
# runtime: 572 ms
# memory: 22.9 MB

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
        end = set()
        for i, rt in enumerate(routes):
            if S in rt:
                q.append(i)
                visited[i] = 1
            if T in rt:
                end.add(i)
        steps = 1
        while q:
            for _ in range(len(q)):
                i = q.popleft()
                if i in end:
                    return steps 
                for j in g[i]:
                    if not visited[j]:
                        visited[j] = 1
                        q.append(j)
            steps += 1
        return -1