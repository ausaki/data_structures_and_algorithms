# title: asteroid-collision
# detail: https://leetcode.com/submissions/detail/364583963/
# datetime: Fri Jul 10 13:19:27 2020
# runtime: 116 ms
# memory: 15.6 MB

class Solution:
    def asteroidCollision(self, soldiers: List[int]) -> List[int]:
        dead = set()
        stack = collections.deque()
        for i in range(len(soldiers)):
            s = soldiers[i]
            m = stack[0] if stack else 0
            if s < 0:
                k = m + s
                if k >= 0:
                    dead.add(i)
                if k < 0:
                    stack = collections.deque()
                if k == 0:
                    stack.popleft()
            else:
                if s >= m: stack.appendleft(s)
        stack = collections.deque()
        for i in range(len(soldiers) - 1, -1, -1):
            s = soldiers[i]
            m = stack[0] if stack else 0
            if s > 0:
                k = m + s
                if k <= 0: dead.add(i)
                if k > 0: stack = collections.deque()
                if k == 0: stack.popleft()
            else:
                if s <= m: stack.appendleft(s)
        return [soldiers[i] for i in range(len(soldiers)) if i not in dead]