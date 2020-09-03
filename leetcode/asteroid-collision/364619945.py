# title: asteroid-collision
# detail: https://leetcode.com/submissions/detail/364619945/
# datetime: Fri Jul 10 14:59:19 2020
# runtime: 100 ms
# memory: 15 MB

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        survivors = []
        for a in asteroids:
            if a > 0:
                survivors.append(a)
            else:
                a = abs(a)
                while survivors and 0 < survivors[-1] < a:
                    survivors.pop()
                if not survivors or survivors[-1] < 0:
                    survivors.append(-a)
                elif survivors[-1] == a:
                    survivors.pop()
        return survivors
                    