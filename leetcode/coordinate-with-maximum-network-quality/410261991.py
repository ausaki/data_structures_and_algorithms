# title: coordinate-with-maximum-network-quality
# detail: https://leetcode.com/submissions/detail/410261991/
# datetime: Sun Oct 18 23:08:04 2020
# runtime: 2120 ms
# memory: 14.1 MB

class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        min_x, min_y, max_x, max_y = 50, 50, 0, 0
        for x, y, _ in towers:
            min_x = min(min_x, x)
            min_y = min(min_y, y)
            max_x = max(max_x, x)
            max_y = max(max_y, y)
        X, Y = 0, 0
        network_quality = 0
        for x in range(min_x, max_x + 1):
            for y in range(min_y, max_y + 1):
                nq = 0
                for x0, y0, q in towers:
                    d = (x - x0) ** 2 + (y - y0) ** 2
                    if d <= radius ** 2:
                        nq += q // (1 + math.sqrt(d))
                if nq > network_quality:
                    network_quality = nq
                    X, Y = x, y
                elif nq == network_quality:
                    if (x, y) < (X, Y):
                        X, Y = x, y
        return X, Y
        