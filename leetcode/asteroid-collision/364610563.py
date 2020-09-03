# title: asteroid-collision
# detail: https://leetcode.com/submissions/detail/364610563/
# datetime: Fri Jul 10 14:32:57 2020
# runtime: 244 ms
# memory: 15.3 MB

class Solution:
    def asteroidCollision(self, soldiers: List[int]) -> List[int]:
        stack = collections.deque()
        survivors = []
        for s in soldiers:
            if s > 0:
                stack.append(s)
            else:
                s = abs(s)
                while stack and s > stack[-1]:
                    stack.pop()
                if not stack:
                    survivors.append(-s)
                elif stack[-1] == s:
                    stack.pop()
        survivors.extend(stack)
        return survivors
                    