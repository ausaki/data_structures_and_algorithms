# title: minimum-jumps-to-reach-home
# detail: https://leetcode.com/submissions/detail/420438081/
# datetime: Sun Nov 15 15:20:20 2020
# runtime: 84 ms
# memory: 14.5 MB

class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        M = max(max(forbidden), x) + b + a
        q = collections.deque([(0, 0)])
        visited = [False] * (M + 1)
        visited[0] = True
        for i in forbidden:
            visited[i] = True
        while q:
            for _ in range(len(q)):
                i, d = q.popleft()
                if i == x:
                    return d
                if i - b > 0 and not visited[i - b]:
                    visited[i - b] = True
                    if i - b == x:
                        return d + 1
                    if i - b + a <= M and not visited[i - b + a]:
                        visited[i - b + a] = True
                        q.append((i - b + a, d + 2))
                if i + a <= M and not visited[i + a]:
                    visited[i + a] = True
                    q.append((i + a, d + 1))
        return -1
    
