# title: asteroid-collision
# detail: https://leetcode.com/submissions/detail/364580520/
# datetime: Fri Jul 10 13:09:49 2020
# runtime: 184 ms
# memory: 15.6 MB

class Solution:
    def asteroidCollision(self, soldiers: List[int]) -> List[int]:
        dead = set()
        max_heap = [0]
        for i in range(len(soldiers)):
            print(max_heap)
            s = soldiers[i]
            m = -max_heap[0]
            if s < 0:
                k = m + s
                if k >= 0:
                    dead.add(i)
                if k < 0:
                    max_heap = [0]
                if k == 0:
                    heapq.heappop(max_heap)
            else:
                if s >= m: heapq.heappush(max_heap, -s)
        max_heap = [0]
        for i in range(len(soldiers) - 1, -1, -1):
            s = soldiers[i]
            m = max_heap[0]
            if s > 0:
                k = m + s
                if k <= 0: dead.add(i)
                if k > 0: max_heap = [0]
                if k == 0: heapq.heappop(max_heap)
            else:
                if s <= m: heapq.heappush(max_heap, s)
        return [soldiers[i] for i in range(len(soldiers)) if i not in dead]