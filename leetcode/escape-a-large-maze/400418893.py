# title: escape-a-large-maze
# detail: https://leetcode.com/submissions/detail/400418893/
# datetime: Fri Sep 25 12:51:11 2020
# runtime: 1988 ms
# memory: 21.7 MB

class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        m = 10 ** 6
        n = len(blocked)
        if target in blocked or source in blocked: return False
        if n <= 1: return True
        dxy = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        blocked = set(map(tuple, blocked))
        threshold = 200 * 200
        def bfs(pos, target):
            q = collections.deque([pos])
            visited = {tuple(pos)}
            cnt = 0
            while q:
                x, y = q.popleft()
                if x == target[0] and y == target[1]:
                    return 1
                cnt += 1
                if cnt > threshold:
                    return 2
                for dx, dy in dxy:
                    x_, y_ = x + dx, y + dy
                    if 0 <= x_ < m and 0 <= y_ < m:
                        p = (x_, y_)
                        if p not in visited and p not in blocked:
                            q.append(p)
                            visited.add(p)
            return -1
        
        i = bfs(source, target)
        # print(i)
        if i == 1:
            return True
        if i == -1:
            return False
        j = bfs(target, source)
        # print(j)
        return j == 2
                     
        
            