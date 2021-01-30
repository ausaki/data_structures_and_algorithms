# title: building-boxes
# detail: https://leetcode.com/submissions/detail/447071327/
# datetime: Sun Jan 24 14:36:07 2021
# runtime: 28 ms
# memory: 14.3 MB

class Solution:
    def minimumBoxes(self, n: int) -> int:
        '''
        一开始的思路跑偏了, 我是从正向思维是思考的: 给定 n 个小立方体最少有多少个会接触地面.
        
        我已经发现了如何使接触地面的小立方体最少的放置方法.
        '''
        
        t = 0
        s = 0
        for i in range(1, n + 1):
            s += i
            if t + s == n:
                return s
            if t + s < n:
                t += s
            else:
                break
        n -= t
        x = math.ceil((math.sqrt(1 + 8 * n) - 1) / 2)
        return s - i + x