# title: keys-and-rooms
# detail: https://leetcode.com/submissions/detail/408489595/
# datetime: Wed Oct 14 12:04:19 2020
# runtime: 64 ms
# memory: 14.4 MB

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        q = collections.deque([0])
        visited = [0] * n
        visited[0] = 1
        while q:
            i = q.popleft()
            n -= 1
            if n == 0:
                return True
            for j in rooms[i]:
                if not visited[j]:
                    visited[j] = 1
                    q.append(j)
        return False