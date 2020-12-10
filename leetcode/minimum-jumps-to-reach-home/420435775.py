# title: minimum-jumps-to-reach-home
# detail: https://leetcode.com/submissions/detail/420435775/
# datetime: Sun Nov 15 15:11:56 2020
# runtime: 84 ms
# memory: 14.4 MB

class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        M = max(max(forbidden), x) + b + a
        q = collections.deque([0])
        dist = [math.inf] * (M + 1)
        dist[0] = 0
        for i in forbidden:
            if i <= M:
                dist[i] = -1
        while q:
            i = q.popleft()
            if i == x:
                return dist[i]
            if i - b > 0 and dist[i] + 1 < dist[i - b]:
                dist[i - b] = dist[i] + 1
                if i - b == x:
                    return dist[i - b]
                if i - b + a <= M and dist[i] + 2 < dist[i - b + a]:
                    dist[i - b + a] = dist[i] + 2
                    q.append(i - b + a)
            if i + a <= M and dist[i] + 1 < dist[i + a]:
                dist[i + a] = dist[i] + 1
                q.append(i + a)
        return -1
    
