# title: asteroid-collision
# detail: https://leetcode.com/submissions/detail/364618098/
# datetime: Fri Jul 10 14:54:01 2020
# runtime: 120 ms
# memory: 15 MB

class Solution(object):
    def asteroidCollision(self, asteroids):
        ans = []
        for new in asteroids:
            while ans and new < 0 < ans[-1]:
                if ans[-1] < -new:
                    ans.pop()
                    continue
                elif ans[-1] == -new:
                    ans.pop()
                break
            else:
                ans.append(new)
        return ans