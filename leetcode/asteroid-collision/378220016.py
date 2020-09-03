# title: asteroid-collision
# detail: https://leetcode.com/submissions/detail/378220016/
# datetime: Sun Aug  9 12:05:57 2020
# runtime: 160 ms
# memory: 14.9 MB

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        survivors = []
        n = len(asteroids)
        i = 0
        while i < n:
            a = asteroids[i]
            if a > 0:
                survivors.append(a)
                i += 1
                continue
            a = abs(a)
            while survivors and survivors[-1] > 0 and survivors[-1] < a:
                survivors.pop()
            if not survivors or survivors[-1] < 0:
                survivors.append(-a)
                i += 1
                continue
            if survivors[-1] == a:
                survivors.pop()
            i += 1
        return survivors
                    