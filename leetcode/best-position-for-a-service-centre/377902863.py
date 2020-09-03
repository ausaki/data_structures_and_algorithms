# title: best-position-for-a-service-centre
# detail: https://leetcode.com/submissions/detail/377902863/
# datetime: Sat Aug  8 23:00:33 2020
# runtime: 236 ms
# memory: 14 MB

class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        n = len(positions)
        x, y = 0, 0
        for x_, y_ in positions:
            x += x_
            y += y_
        x /= n
        y /= n
        result = float('inf')
        step = 50
        
        def distance(x, y):
            dis = 0
            for x_, y_ in positions:
                d = math.sqrt((x - x_) ** 2 + (y - y_) ** 2)
                dis += d
            return dis
        
        while step > 1e-6:
            d0 = distance(x, y)
            for dx, dy in [(-step, 0), (step, 0), (0, -step), (0, step)]:
                x_, y_ = x + dx, y + dy
                d1 = distance(x_, y_)                
                if d1 < d0:
                    result = min(result, d1)
                    x, y = x_, y_
                    break
            else:
                result = min(result, d0)
                step /= 2
        return result